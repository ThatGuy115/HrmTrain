﻿label main_ex_CharacterExItem_constants:
    # main zOrders
    define G_Z_UNDERLEGS = 0
    define G_Z_LEGS = 20
    define G_Z_PANTIES = 40
    define G_Z_SKIRT = 60
    define G_Z_HANDS = 80
    define G_Z_BODY = 100
    define G_Z_TITS = 120
    define G_Z_DRESS = 140
    define G_Z_FACE = 300
    
    # additional zOrders
    define G_Z_HEADWEAR = 160
    define G_Z_POSE = 180

    # here is the keys for additional items
    define G_N_SKIRT = 'skirt'
    define G_N_BADGE = 'badge'
    define G_N_NETS = 'nets'
    
    return

init -998 python:
    from copy import deepcopy 

    class CharacterExItem(store.object):
        # some kind of enumerator
        _indSelfAdded = CharacterExItemAction._indSelfAdded
        _indSelfRemoved = CharacterExItemAction._indSelfRemoved
        _indItemAdded = CharacterExItemAction._indItemAdded
        _indItemRemoved = CharacterExItemAction._indItemRemoved
        _indItemShown = CharacterExItemAction._indItemShown
        _indItemHidden = CharacterExItemAction._indItemHidden
        _indStyleBeforeChange = CharacterExItemAction._indStyleBeforeChange
        _indStyleAfterChange = CharacterExItemAction._indStyleAfterChange
        _indItemCount = CharacterExItemAction._indItemCount

        # creates variables
        def __init__( self ):
            # being sub item means do not trigger any actions.
            # state of subitem is equal to state of subitem owner
            # e.g. is we change the style of owner, the style of subitem will also be changed,
            # or if we hide the owner, subitem will also be hidden and so on
            self.mIsSubitem = False
            self.mSubitems = [] # list of keys of subitems
            self.mKey = ""
            self.mName = ""
            self.mIsVisible = True
            self.mFileName = ""
            self.mFileFolder = ""
            self.mStyles = []   # list with names of styles
            self.mActiveStyle = None  # name of current active style
            self.mOwner = None # pointer to CharacterExData - container where item is currently assigned
            self.mXmlLinkerKey = "" # key from which creator was this item created

            # public
            self.image = None
            self.zorder = 0
            self.position = Transform( pos = ( 0, 0 ) )            
            # parent of item, should be string key or None. When parent item is hidden, this item also hide, and the same with showing parent
            self.parent = None

            # here is the list of keys to hide with this item
            self.mHideList = []
            
            # stuff for actions
            # self.mActions is an array of arrays
            self.mActions = []
            for num in range( CharacterExItem._indItemCount ):
                self.mActions.append( [] )

            # map with transforms
            self.mTransforms = {}

            # map with transforms from owner
            self.mOwnerTransforms = {}

            # here we'll store all items, which affects visibility of this item
            # items, stored here, change the visibility to FALSE
            self.mDirectors = set()

        # old constructor
        @classmethod
        def createOld( cls, aFolder, aName, aOrder, aParent = None, aPos = None ):
            item = cls()

            item.mFileName = aName
            item.mFileFolder = aFolder
            item.image = aFolder + aName
            item.zorder = aOrder
            item.position = Transform( pos = ( 0, 0 ) ) 
            if aPos is not None:
                item.position = aPos
            # parent of item, should be string key or None. When parent item is hidden, this item also hide, and the same with showing parent
            item.parent = aParent

            # here is the list of keys to hide with this item
            item._fillHideList()
            return item

        # constructor for copying
        @classmethod
        def fromItem( cls, aItem ):
            item = cls()
            item.mKey = aItem.mKey
            item.mName = aItem.mName
            item.mIsVisible = aItem.mIsVisible
            item.mFileName = aItem.mFileName
            item.mFileFolder = aItem.mFileFolder
            item.mStyles = list( aItem.mStyles )
            item.mActiveStyle = aItem.mActiveStyle
            item.mOwner = aItem.mOwner
            item.mXmlLinkerKey = aItem.mXmlLinkerKey

            # public
            item.zorder = aItem.zorder
            item.position = Transform( pos = ( aItem.position.xpos, aItem.position.ypos ) )
            item.image = aItem.image
            # parent of item, should be string key or None. When parent item is hidden, this item also hide, and the same with showing parent
            item.parent = aItem.parent

            # here is the list of keys to hide with this item
            item.mHideList = list( aItem.mHideList )
            
            # stuff for actions
            # self.mActions is an array of arrays
            item.mActions = deepcopy( aItem.mActions )

            # map with transforms
            item.mTransforms = deepcopy( item.mTransforms )

            # owner transforms
            item.mOwnerTransforms = deepcopy( aItem.mOwnerTransforms )

            # here we'll store all items, which affects visibility of this item
            # items, stored here, change the visibility to FALSE
            item.mDirectors = set( aItem.mDirectors )
            return item

        # new constructor
        @classmethod
        def fromDesc( cls, aDescription, aXmlLinkerKey ):
            item = cls()

            item.mXmlLinkerKey = aXmlLinkerKey
            item.mKey = aDescription.mKey
            item.mName = aDescription.mName
            item.mStyles = aDescription.mStyles.keys()   # list with only style names, will get the styles from ItemBase

            # set current style to 'default'
            item.setStyle( 'default' )
            item._fillHideList()
            return item

        # static constructor to create from description
        @classmethod
        def create( cls, aDescription, aXmlLinkerKey ):
            item = cls.fromDesc( aDescription, aXmlLinkerKey )
            return item


        ##########################################################
        # change style method
        ##########################################################        

        def setStyle( self, aStyleName ):
            if aStyleName in self.mStyles:
                if self.mActiveStyle != None:
                    self._discardCurrentStyle()
                self.mActiveStyle = aStyleName
                self._applyStyle( aStyleName )

        def getStyle( self ):
            return self.mActiveStyle

        ##########################################################
        # call this to change only image of the item ( including path and name )
        ##########################################################  

        # used for face changing
        def changeImage( self, aImageFolder, aImageName ):
            self.mFileName = aImageName
            self.mFileFolder = aImageFolder
            self.image = aImageFolder + aImageName

        ##########################################################
        # modify image methods
        ##########################################################
        
        def updateImage( self, aImage ):
            # here we can change image ( for example, make im.Flip action to the image, and save it here )
            self.image = aImage
        
        def getImage( self ):
            return self.image
            
        ##########################################################
        # show/hide methods
        ##########################################################

        def hide( self, aSource ):
            prevVis = self.mIsVisible
            self._hideInner( aSource )
            if prevVis != self.mIsVisible:
                self.mOwner._onItemHidden( self )
                for inKey in self.mHideList:
                    self.mOwner.showItemKey( inKey, self.mName )
                
        def show( self, aSource ):
            prevVis = self.mIsVisible            
            self._showInner( aSource )
            if prevVis != self.mIsVisible:
                self.mOwner._onItemShown( self )
                for inKey in self.mHideList:
                    self.mOwner.hideItemKey( inKey, self.mName )    

        ##########################################################
        # methods for proper transform work
        ##########################################################

        def addTransform( self, aName, aTransform, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._addTransform( trDict, aName, aTransform )
                
        def delTransform( self, aName, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._delTransform( trDict, aName )

        def clearTransforms( self, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._clearTransforms( trDict )

        def getTransform( self, aName, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            return self._getTransform( trDict, aName )
            
        ##########################################################
        # inner callbacks, do not use them directly
        ##########################################################            

        def onSelfAdded( self, aKey, aItems, aCharacterEx ):
            self.mOwner = aCharacterEx
            self.mKey = aKey
            if self.parent in aItems:
                if not aItems[ self.parent ].mIsVisible:
                    self._hideInner( 'parent' )
            self.innerOnSelfAdded( aItems )

        def onSelfRemoved( self, aItems, aCharacterEx ):
            self.innerOnSelfRemoved( aItems )
            self.mOwner = None
        
        def onItemAdded( self, aItem ):
            self.innerOnItemAdded( aItem )
            
        def onItemRemoved( self, aItem ):
            if aItem.mKey == self.parent:
                self._showInner( 'parent' )
            self.innerOnItemRemoved( aItem )
            
        def onItemHidden( self, aItem ):
            if aItem.mKey == self.parent:
                self._hideInner( 'parent' )
            self.innerOnItemHidden( aItem )
            
        def onItemShown( self, aItem ):
            if aItem.mKey == self.parent:
                self._showInner( 'parent' )
            self.innerOnItemShown( aItem )

        def onItemStyleBeforeChange( self, aItem ):
            self.innerOnItemStyleBeforeChange( aItem )

        def onItemStyleAfterChange( self, aItem ):
            self.innerOnItemStyleAfterChange( aItem )

        ##########################################################
        # methods to forget about them :D
        ##########################################################
        def _hideInner( self, aSource ):
            self.mIsVisible = False
            self.mDirectors.add( aSource )
                
        def _showInner( self, aSource ):
            self.mDirectors.discard( aSource )
            if not self.mDirectors:
                self.mIsVisible = True

        ##########################################################
        def _getTransformDict( self, aIsInner ):
            if aIsInner:
                return self.mTransforms
            else:
                return self.mOwnerTransforms

        def _addTransform( self, aTransformDic, aName, aTransform ):
            if aName in aTransformDic.keys():
                tr = aTransformDic[ aName ]
                del aTransformDic[ aName ]
                self.image = tr.discard( self.image )
            self.image = aTransform.apply( self.image )
            aTransformDic[ aName ] = aTransform

        def _delTransform( self, aTransformDic, aName ):
            if aName in aTransformDic.keys():
                tr = aTransformDic[ aName ]
                del aTransformDic[ aName ]
                self.image = tr.discard( self.image )

        def _clearTransforms( self, aTransformDic ):
            keys = aTransformDic.keys()
            for key in keys:
                self._delTransform( aTransformDic, key )

        def _getTransform( self, aTransformDic, aName ):
            if aName in aTransformDic.keys():
                return aTransformDic[ aName ]
            else:
                return None

        ##########################################################
        def _applyAction( self, aIndex, aCharacterEx, aEventSenderItem, aItemsAll = None ):
            if self.mOwner == None:
                return
            else:
                if aItemsAll == None:
                    aItemsAll = self.mOwner.getAllItems()

            for action in self.mActions[ aIndex ]:
                action.act( self, aEventSenderItem, aCharacterEx, aItemsAll )

        ##########################################################
        def _applyStyle( self, aStyleName ):
            desc = WTXmlLinker.i( self.mXmlLinkerKey ).getItemStyle( self.mName, aStyleName )

            if desc.mFrame != None:
                self.mFileName = desc.mFrame
            if desc.mFileFolder != None:
                self.mFileFolder = desc.mFileFolder

            if desc.mFrame != None or desc.mFileFolder != None:
                self.image = self.mFileFolder + self.mFileName
            if desc.mZOrder != None:
                self.zorder = desc.mZOrder
            if desc.mShift != None:
                self.position = Transform( pos = ( desc.mShift.xpos, desc.mShift.ypos ) )
            if desc.mParent != None:
                self.parent = desc.mParent
            if desc.mIsVisible != None:
                self.mIsVisible = desc.mIsVisible

            if desc.mHideList != None:
                del self.mHideList[:]
                for elem in desc.mHideList:
                    self.mHideList.append( elem )
            
            # map with transforms
            if desc.mTransforms != None:
                self.mTransforms.clear()
                for key,val in desc.mTransforms.iteritems():
                    self.addTransform( key, CharacterExTransform.create( val ), True )


            if desc.mActions != None:
                # clear actions
                for elem in self.mActions:
                    del elem[:]
                # create new
                for actDesc in desc.mActions:
                    actNew = CharacterExItemAction.create( actDesc )
                    if actNew.mIndex != -1:
                        self.mActions[ actNew.mIndex ].append( actNew )

            # hide need-to-hide items and check actions
            if self.mOwner != None:
                #check for items in directors - if there any, hide item
                if self.mDirectors:
                    self.mIsVisible = False
                # hide items from HideList only if current item is visible
                if self.mIsVisible:
                    for key in self.mHideList:
                        self.mOwner.hideItemKey( key, self.mName )
                # say to owner that we've changed the style
                self.mOwner._onItemStyleAfterChange( self )
                # and we should apply all owner's transforms
                for tr in self.mOwnerTransforms.values():
                    self.image = tr.apply( self.image )

        def _discardCurrentStyle( self ):
            # say to owner that we are changing the style
            if self.mOwner != None:
                self.mOwner._onItemStyleBeforeChange( self )
            # clear transforms from this style
            self.clearTransforms()
            # show need-to-hide items
            if self.mOwner != None:
                for key in self.mHideList:
                    self.mOwner.showItemKey( key, self.mName )

        ##########################################################
        # methods to override
        ##########################################################

        def _fillHideList( self ):
            # the easiest way to hide other items by this one - add their keys to the self.mHideList in a way:
            # self.mHideList.append( 'name' )
            None
        
        def innerOnSelfAdded( self, aItems ):
            # this called when THIS item is added to Hermione
            # we can add additional items, needed for this item, to HermioneView
            for key in self.mHideList:
                self.mOwner.hideItemKey( key, self.mName )
            self._applyAction( CharacterExItem._indSelfAdded, self.mOwner, self, aItems )
            
        def innerOnSelfRemoved( self, aItems ):
            # this called just after deleting SELF from Hermione
            for key in self.mHideList:
                self.mOwner.showItemKey( key, self.mName )
            self._applyAction( CharacterExItem._indSelfRemoved, self.mOwner, self, aItems )
        
        def innerOnItemAdded( self, aItem ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            if aItem.mKey in self.mHideList:
                self.mOwner.hideItemKey( aItem.mKey, self.mName )
            self._applyAction( CharacterExItem._indItemAdded, self.mOwner, aItem )
            
        def innerOnItemRemoved( self, aItem ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            # item is removed... fuck all!
            #if aItemKey in self.mHideList:
            #    aCharacterEx.showItemKey( aItemKey, self.mName )
            self._applyAction( CharacterExItem._indItemRemoved, self.mOwner, aItem )

        def innerOnItemHidden( self, aItem ):
            # this called when other item is hidden
            self._applyAction( CharacterExItem._indItemHidden, self.mOwner, aItem )
            
        def innerOnItemShown( self, aItem ):
            # this called when other item is shown
            self._applyAction( CharacterExItem._indItemShown, self.mOwner, aItem )

        def innerOnItemStyleBeforeChange( self, aItem ):
            # this called when this item or other item will change the style
            self._applyAction( CharacterExItem._indStyleBeforeChange, self.mOwner, aItem )

        def innerOnItemStyleAfterChange( self, aItem ):
            # this called when this item or other item has changed the style
            self._applyAction( CharacterExItem._indStyleAfterChange, self.mOwner, aItem )
           