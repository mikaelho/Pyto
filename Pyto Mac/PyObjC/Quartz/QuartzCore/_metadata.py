# This file is generated by objective.metadata
#
# Last update: Tue Jun 26 07:59:02 2018

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'CATransform3D': objc.createStructType('CATransform3D', sel32or64(b'{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}'), ['m11', 'm12', 'm13', 'm14', 'm21', 'm22', 'm23', 'm24', 'm31', 'm32', 'm33', 'm34', 'm41', 'm42', 'm43', 'm44'])})
constants = '''$CIDetectorAccuracy$CIDetectorAccuracyHigh$CIDetectorAccuracyLow$CIDetectorAspectRatio$CIDetectorEyeBlink$CIDetectorFocalLength$CIDetectorImageOrientation$CIDetectorMaxFeatureCount$CIDetectorMinFeatureSize$CIDetectorNumberOfAngles$CIDetectorReturnSubFeatures$CIDetectorSmile$CIDetectorTracking$CIDetectorTypeFace$CIDetectorTypeQRCode$CIDetectorTypeRectangle$CIDetectorTypeText$CIFeatureTypeFace$CIFeatureTypeQRCode$CIFeatureTypeRectangle$CIFeatureTypeText$kCAAlignmentCenter$kCAAlignmentJustified$kCAAlignmentLeft$kCAAlignmentNatural$kCAAlignmentRight$kCAAnimationCubic$kCAAnimationCubicPaced$kCAAnimationDiscrete$kCAAnimationLinear$kCAAnimationPaced$kCAAnimationRotateAuto$kCAAnimationRotateAutoReverse$kCAContentsFormatGray8Uint$kCAContentsFormatRGBA16Float$kCAContentsFormatRGBA8Uint$kCAEmitterBehaviorAlignToMotion$kCAEmitterBehaviorAttractor$kCAEmitterBehaviorColorOverLife$kCAEmitterBehaviorDrag$kCAEmitterBehaviorLight$kCAEmitterBehaviorSimpleAttractor$kCAEmitterBehaviorValueOverLife$kCAEmitterBehaviorWave$kCAEmitterLayerAdditive$kCAEmitterLayerBackToFront$kCAEmitterLayerCircle$kCAEmitterLayerCuboid$kCAEmitterLayerLine$kCAEmitterLayerOldestFirst$kCAEmitterLayerOldestLast$kCAEmitterLayerOutline$kCAEmitterLayerPoint$kCAEmitterLayerPoints$kCAEmitterLayerRectangle$kCAEmitterLayerSphere$kCAEmitterLayerSurface$kCAEmitterLayerUnordered$kCAEmitterLayerVolume$kCAFillModeBackwards$kCAFillModeBoth$kCAFillModeForwards$kCAFillModeFrozen$kCAFillModeRemoved$kCAFillRuleEvenOdd$kCAFillRuleNonZero$kCAFilterLinear$kCAFilterNearest$kCAFilterTrilinear$kCAGradientLayerAxial$kCAGradientLayerConic$kCAGradientLayerRadial$kCAGravityBottom$kCAGravityBottomLeft$kCAGravityBottomRight$kCAGravityCenter$kCAGravityLeft$kCAGravityResize$kCAGravityResizeAspect$kCAGravityResizeAspectFill$kCAGravityRight$kCAGravityTop$kCAGravityTopLeft$kCAGravityTopRight$kCALineCapButt$kCALineCapRound$kCALineCapSquare$kCALineJoinBevel$kCALineJoinMiter$kCALineJoinRound$kCAMediaTimingFunctionDefault$kCAMediaTimingFunctionEaseIn$kCAMediaTimingFunctionEaseInEaseOut$kCAMediaTimingFunctionEaseOut$kCAMediaTimingFunctionLinear$kCAOnOrderIn$kCAOnOrderOut$kCARendererColorSpace$kCARendererMetalCommandQueue$kCAScrollBoth$kCAScrollHorizontally$kCAScrollNone$kCAScrollVertically$kCATransactionAnimationDuration$kCATransactionAnimationTimingFunction$kCATransactionCompletionBlock$kCATransactionDisableActions$kCATransition$kCATransitionFade$kCATransitionFromBottom$kCATransitionFromLeft$kCATransitionFromRight$kCATransitionFromTop$kCATransitionMoveIn$kCATransitionPush$kCATransitionReveal$kCATruncationEnd$kCATruncationMiddle$kCATruncationNone$kCATruncationStart$kCAValueFunctionRotateX$kCAValueFunctionRotateY$kCAValueFunctionRotateZ$kCAValueFunctionScale$kCAValueFunctionScaleX$kCAValueFunctionScaleY$kCAValueFunctionScaleZ$kCAValueFunctionTranslate$kCAValueFunctionTranslateX$kCAValueFunctionTranslateY$kCAValueFunctionTranslateZ$kCIActiveKeys$kCIApplyOptionColorSpace$kCIApplyOptionDefinition$kCIApplyOptionExtent$kCIApplyOptionUserInfo$kCIAttributeClass$kCIAttributeDefault$kCIAttributeDescription$kCIAttributeDisplayName$kCIAttributeFilterAvailable_Mac$kCIAttributeFilterAvailable_iOS$kCIAttributeFilterCategories$kCIAttributeFilterDisplayName$kCIAttributeFilterName$kCIAttributeIdentity$kCIAttributeMax$kCIAttributeMin$kCIAttributeName$kCIAttributeReferenceDocumentation$kCIAttributeSliderMax$kCIAttributeSliderMin$kCIAttributeType$kCIAttributeTypeAngle$kCIAttributeTypeBoolean$kCIAttributeTypeColor$kCIAttributeTypeCount$kCIAttributeTypeDistance$kCIAttributeTypeGradient$kCIAttributeTypeImage$kCIAttributeTypeInteger$kCIAttributeTypeOffset$kCIAttributeTypeOpaqueColor$kCIAttributeTypePosition$kCIAttributeTypePosition3$kCIAttributeTypeRectangle$kCIAttributeTypeScalar$kCIAttributeTypeTime$kCIAttributeTypeTransform$kCICategoryBlur$kCICategoryBuiltIn$kCICategoryColorAdjustment$kCICategoryColorEffect$kCICategoryCompositeOperation$kCICategoryDistortionEffect$kCICategoryFilterGenerator$kCICategoryGenerator$kCICategoryGeometryAdjustment$kCICategoryGradient$kCICategoryHalftoneEffect$kCICategoryHighDynamicRange$kCICategoryInterlaced$kCICategoryNonSquarePixels$kCICategoryReduction$kCICategorySharpen$kCICategoryStillImage$kCICategoryStylize$kCICategoryTileEffect$kCICategoryTransition$kCICategoryVideo$kCIContextCacheIntermediates$kCIContextHighQualityDownsample$kCIContextOutputColorSpace$kCIContextOutputPremultiplied$kCIContextPriorityRequestLow$kCIContextUseSoftwareRenderer$kCIContextWorkingColorSpace$kCIContextWorkingFormat$kCIFilterGeneratorExportedKey$kCIFilterGeneratorExportedKeyName$kCIFilterGeneratorExportedKeyTargetObject$kCIFormatA16@i$kCIFormatA8@i$kCIFormatABGR8@i$kCIFormatARGB8@i$kCIFormatAf@i$kCIFormatAh@i$kCIFormatBGRA8@i$kCIFormatL16@i$kCIFormatL8@i$kCIFormatLA16@i$kCIFormatLA8@i$kCIFormatLAf@i$kCIFormatLAh@i$kCIFormatLf@i$kCIFormatLh@i$kCIFormatR16@i$kCIFormatR8@i$kCIFormatRG16@i$kCIFormatRG8@i$kCIFormatRGBA16@i$kCIFormatRGBA8@i$kCIFormatRGBAf@i$kCIFormatRGBAh@i$kCIFormatRGf@i$kCIFormatRGh@i$kCIFormatRf@i$kCIFormatRh@i$kCIImageApplyOrientationProperty$kCIImageAutoAdjustCrop$kCIImageAutoAdjustEnhance$kCIImageAutoAdjustFeatures$kCIImageAutoAdjustLevel$kCIImageAutoAdjustRedEye$kCIImageAuxiliaryDepth$kCIImageAuxiliaryDisparity$kCIImageAuxiliaryPortraitEffectsMatte$kCIImageColorSpace$kCIImageNearestSampling$kCIImageProperties$kCIImageProviderTileSize$kCIImageProviderUserInfo$kCIImageRepresentationAVDepthData$kCIImageRepresentationAVPortraitEffectsMatte$kCIImageRepresentationDepthImage$kCIImageRepresentationDisparityImage$kCIImageRepresentationPortraitEffectsMatteImage$kCIImageTextureFormat$kCIImageTextureTarget$kCIInputAllowDraftModeKey$kCIInputAmountKey$kCIInputAngleKey$kCIInputAspectRatioKey$kCIInputBackgroundImageKey$kCIInputBaselineExposureKey$kCIInputBiasKey$kCIInputBoostKey$kCIInputBoostShadowAmountKey$kCIInputBrightnessKey$kCIInputCenterKey$kCIInputColorKey$kCIInputColorNoiseReductionAmountKey$kCIInputContrastKey$kCIInputDecoderVersionKey$kCIInputDepthImageKey$kCIInputDisableGamutMapKey$kCIInputDisparityImageKey$kCIInputEVKey$kCIInputEnableChromaticNoiseTrackingKey$kCIInputEnableSharpeningKey$kCIInputEnableVendorLensCorrectionKey$kCIInputExtentKey$kCIInputGradientImageKey$kCIInputIgnoreImageOrientationKey$kCIInputImageKey$kCIInputImageOrientationKey$kCIInputIntensityKey$kCIInputLinearSpaceFilter$kCIInputLuminanceNoiseReductionAmountKey$kCIInputMaskImageKey$kCIInputMatteImageKey$kCIInputMoireAmountKey$kCIInputNeutralChromaticityXKey$kCIInputNeutralChromaticityYKey$kCIInputNeutralLocationKey$kCIInputNeutralTemperatureKey$kCIInputNeutralTintKey$kCIInputNoiseReductionAmountKey$kCIInputNoiseReductionContrastAmountKey$kCIInputNoiseReductionDetailAmountKey$kCIInputNoiseReductionSharpnessAmountKey$kCIInputRadiusKey$kCIInputRefractionKey$kCIInputSaturationKey$kCIInputScaleFactorKey$kCIInputScaleKey$kCIInputShadingImageKey$kCIInputSharpnessKey$kCIInputTargetImageKey$kCIInputTimeKey$kCIInputTransformKey$kCIInputVersionKey$kCIInputWeightsKey$kCIInputWidthKey$kCIOutputImageKey$kCIOutputNativeSizeKey$kCISamplerAffineMatrix$kCISamplerColorSpace$kCISamplerFilterLinear$kCISamplerFilterMode$kCISamplerFilterNearest$kCISamplerWrapBlack$kCISamplerWrapClamp$kCISamplerWrapMode$kCISupportedDecoderVersionsKey$kCIUIParameterSet$kCIUISetAdvanced$kCIUISetBasic$kCIUISetDevelopment$kCIUISetIntermediate$'''
constants = constants + '$CATransform3DIdentity@%s$'%(sel32or64('{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}'),)
enums = '''$CA_WARN_DEPRECATED@1$CIDataMatrixCodeECCVersion000@0$CIDataMatrixCodeECCVersion050@50$CIDataMatrixCodeECCVersion080@80$CIDataMatrixCodeECCVersion100@100$CIDataMatrixCodeECCVersion140@140$CIDataMatrixCodeECCVersion200@200$CIQRCodeErrorCorrectionLevelH@72$CIQRCodeErrorCorrectionLevelL@76$CIQRCodeErrorCorrectionLevelM@77$CIQRCodeErrorCorrectionLevelQ@81$CIRenderDestinationAlphaNone@0$CIRenderDestinationAlphaPremultiplied@1$CIRenderDestinationAlphaUnpremultiplied@2$kCAConstraintHeight@7$kCAConstraintMaxX@2$kCAConstraintMaxY@6$kCAConstraintMidX@1$kCAConstraintMidY@5$kCAConstraintMinX@0$kCAConstraintMinY@4$kCAConstraintWidth@3$kCALayerBottomEdge@4$kCALayerHeightSizable@16$kCALayerLeftEdge@1$kCALayerMaxXMargin@4$kCALayerMaxXMaxYCorner@8$kCALayerMaxXMinYCorner@2$kCALayerMaxYMargin@32$kCALayerMinXMargin@1$kCALayerMinXMaxYCorner@4$kCALayerMinXMinYCorner@1$kCALayerMinYMargin@8$kCALayerNotSizable@0$kCALayerRightEdge@2$kCALayerTopEdge@8$kCALayerWidthSizable@2$'''
misc.update({})
functions={'CATransform3DIsAffine': (sel32or64(b'B{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DInvert': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DIsIdentity': (sel32or64(b'B{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeScale': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DTranslate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DEqualToTransform': (sel32or64(b'B{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DRotate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}dddd'),), 'CACurrentMediaTime': (b'd',), 'CATransform3DMakeRotation': (sel32or64(b'{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}dddd'),), 'CATransform3DConcat': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DScale': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DMakeTranslation': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DGetAffineTransform': (sel32or64(b'{CGAffineTransform=ffffff}{CATransform3D=ffffffffffffffff}', b'{CGAffineTransform=dddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeAffineTransform': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CGAffineTransform=ffffff}', b'{CATransform3D=dddddddddddddddd}{CGAffineTransform=dddddd}'),)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CAAnimation', b'isRemovedOnCompletion', {'retval': {'type': b'Z'}})
    r(b'CAAnimation', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAAnimation', b'setRemovedOnCompletion:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAAnimation', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CAEmitterBehavior', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'CAEmitterBehavior', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAEmitterCell', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'CAEmitterCell', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAEmitterCell', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CAEmitterLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r(b'CAEmitterLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'allowsEdgeAntialiasing', {'retval': {'type': 'Z'}})
    r(b'CALayer', b'allowsGroupOpacity', {'retval': {'type': 'Z'}})
    r(b'CALayer', b'containsPoint:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'contentsAreFlipped', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'drawsAsynchronously', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isDoubleSided', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isGeometryFlipped', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isHidden', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isOpaque', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'masksToBounds', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplay', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplayForKey:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplayOnBoundsChange', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsLayout', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'setAllowsEdgeAntialiasing:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CALayer', b'setAllowsGroupOpacity:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CALayer', b'setDoubleSided:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setDrawsAsynchronously:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setGeometryFlipped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setHidden:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setMasksToBounds:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setNeedsDisplayOnBoundsChange:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setOpaque:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setShouldRasterize:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setWantsExtendedDynamicRangeContent:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CALayer', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'shouldRasterize', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'wantsExtendedDynamicRangeContent', {'retval': {'type': 'Z'}})
    r(b'CAMetalLayer', b'allowsNextDrawableTimeout', {'retval': {'type': 'Z'}})
    r(b'CAMetalLayer', b'displaySyncEnabled', {'retval': {'type': 'Z'}})
    r(b'CAMetalLayer', b'framebufferOnly', {'retval': {'type': 'Z'}})
    r(b'CAMetalLayer', b'presentsWithTransaction', {'retval': {'type': 'Z'}})
    r(b'CAMetalLayer', b'setAllowsNextDrawableTimeout:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAMetalLayer', b'setDisplaySyncEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAMetalLayer', b'setFramebufferOnly:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAMetalLayer', b'setPresentsWithTransaction:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAMetalLayer', b'setWantsExtendedDynamicRangeContent:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAMetalLayer', b'wantsExtendedDynamicRangeContent', {'retval': {'type': 'Z'}})
    r(b'CAOpenGLLayer', b'canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CAOpenGLLayer', b'drawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'arguments': {5: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CAOpenGLLayer', b'isAsynchronous', {'retval': {'type': b'Z'}})
    r(b'CAOpenGLLayer', b'setAsynchronous:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAOpenGLLayer', b'setWantsExtendedDynamicRangeContent:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CAOpenGLLayer', b'wantsExtendedDynamicRangeContent', {'retval': {'type': 'Z'}})
    r(b'CAPropertyAnimation', b'isAdditive', {'retval': {'type': b'Z'}})
    r(b'CAPropertyAnimation', b'isCumulative', {'retval': {'type': b'Z'}})
    r(b'CAPropertyAnimation', b'setAdditive:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAPropertyAnimation', b'setCumulative:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CARenderer', b'beginFrameAtTime:timeStamp:', {'arguments': {3: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CARenderer', b'rendererWithCGLContext:options:', {'arguments': {2: {'type': '^{_CGLContextObject=}'}}})
    r(b'CAReplicatorLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r(b'CAReplicatorLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CATextLayer', b'allowsFontSubpixelQuantization', {'retval': {'type': 'Z'}})
    r(b'CATextLayer', b'font', {'retval': {'type': b'@'}})
    r(b'CATextLayer', b'isWrapped', {'retval': {'type': b'Z'}})
    r(b'CATextLayer', b'setAllowsFontSubpixelQuantization:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CATextLayer', b'setFont:', {'arguments': {2: {'type': b'@'}}})
    r(b'CATextLayer', b'setWrapped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CATransaction', b'completionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'CATransaction', b'disableActions', {'retval': {'type': b'Z'}})
    r(b'CATransaction', b'setCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'CATransaction', b'setDisableActions:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CIAztecCodeDescriptor', b'isCompact', {'retval': {'type': 'Z'}})
    r(b'CIColor', b'components', {'retval': {'c_array_of_variable_length': True}})
    r(b'CIContext', b'createCGImage:fromRect:format:colorSpace:deferred:', {'retval': {'already_cfretained': True}, 'arguments': {6: {'type': 'Z'}}})
    r(b'CIContext', b'createCGLayerWithSize:info:', {'retval': {'already_cfretained': True}})
    r(b'CIContext', b'prepareRender:fromRect:toDestination:atPoint:error:', {'retval': {'type': 'Z'}, 'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CIContext', b'render:toBitmap:rowBytes:bounds:format:colorSpace:', {'arguments': {3: {'type_modifier': b'o', 'c_array_of_variable_length': True}}})
    r(b'CIContext', b'startTaskToClear:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CIContext', b'startTaskToRender:fromRect:toDestination:atPoint:error:', {'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CIContext', b'startTaskToRender:toDestination:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CIContext', b'writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {7: {'type_modifier': b'o'}}})
    r(b'CIContext', b'writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CIContext', b'writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {7: {'type_modifier': b'o'}}})
    r(b'CIFaceFeature', b'hasFaceAngle', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasLeftEyePosition', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasMouthPosition', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasRightEyePosition', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasSmile', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasTrackingFrameCount', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasTrackingID', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'leftEyeClosed', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'rightEyeClosed', {'retval': {'type': b'Z'}})
    r(b'CIFilter', b'apply:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIFilter', b'filterArrayFromSerializedXMP:inputImageExtent:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CIFilter', b'filterWithName:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIFilter', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'CIFilter', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CIFilterGenerator', b'writeToURL:atomically:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}}})
    r(b'CIFilterShape', b'transformBy:interior:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CIImage', b'imageWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIImage', b'imageWithTexture:size:flipped:options:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIImage', b'initWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIImage', b'initWithTexture:size:flipped:options:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIImage', b'writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {7: {'type_modifier': b'o'}}})
    r(b'CIImage', b'writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CIImage', b'writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:', {'retval': {'type': 'Z'}, 'arguments': {7: {'type_modifier': b'o'}}})
    r(b'CIImageProcessorKernel', b'applyWithExtent:inputs:arguments:error:', {'arguments': {5: {'type_modifier': b'o'}}})
    r(b'CIImageProcessorKernel', b'processWithInputs:arguments:output:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'CIKernel', b'applyWithExtent:roiCallback:arguments:', {'arguments': {3: {'callable': {'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'i'}, 2: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}}}}})
    r(b'CIKernel', b'kernelWithFunctionName:fromMetalLibraryData:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CIKernel', b'kernelWithFunctionName:fromMetalLibraryData:outputPixelFormat:error:', {'arguments': {5: {'type_modifier': b'o'}}})
    r(b'CIKernel', b'setROISelector:', {'arguments': {2: {'sel_of_type': sel32or64(b'{CGRect={CGPoint=ff}{CGSize=ff}}@:i{CGRect={CGPoint=ff}{CGSize=ff}}@', b'{CGRect={CGPoint=dd}{CGSize=dd}}@:i{CGRect={CGPoint=dd}{CGSize=dd}}@')}}})
    r(b'CIPDF417CodeDescriptor', b'isCompact', {'retval': {'type': 'Z'}})
    r(b'CIPlugIn', b'loadPlugIn:allowExecutableCode:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CIPlugIn', b'loadPlugIn:allowNonExecutable:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CIRenderDestination', b'blendsInDestinationColorSpace', {'retval': {'type': 'Z'}})
    r(b'CIRenderDestination', b'initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:', {'arguments': {6: {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'CIRenderDestination', b'isClamped', {'retval': {'type': 'Z'}})
    r(b'CIRenderDestination', b'isDithered', {'retval': {'type': 'Z'}})
    r(b'CIRenderDestination', b'isFlipped', {'retval': {'type': 'Z'}})
    r(b'CIRenderDestination', b'setBlendsInDestinationColorSpace:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CIRenderDestination', b'setClamped:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CIRenderDestination', b'setDithered:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CIRenderDestination', b'setFlipped:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CIRenderTask', b'waitUntilCompletedAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'CISampler', b'initWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CISampler', b'samplerWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIVector', b'initWithValues:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'CIVector', b'vectorWithValues:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'CIWarpKernel', b'applyWithExtent:roiCallback:inputImage:arguments:', {'arguments': {3: {'callable': {'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'i'}, 2: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}}}}})
    r(b'NSObject', b'actionForLayer:forKey:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'animationDidStart:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'animationDidStop:finished:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'Z'}}})
    r(b'NSObject', b'autoreverses', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'baseAddress', {'retval': {'type': '^v', 'c_array_of_variable_length': True}})
    r(b'NSObject', b'beginTime', {'required': True, 'retval': {'type': b'd'}})
    r(b'NSObject', b'bytesPerRow', {'retval': {'type': 'L'}})
    r(b'NSObject', b'displayLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'drawLayer:inContext:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'^{CGContext=}'}}})
    r(b'NSObject', b'duration', {'required': True, 'retval': {'type': b'd'}})
    r(b'NSObject', b'fillMode', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'filterWithName:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'format', {'retval': {'type': sel32or64(b'i', b'q')}})
    r(b'NSObject', b'invalidateLayoutOfLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'layoutSublayersOfLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'load:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^v'}}})
    r(b'NSObject', b'preferredSizeOfLayer:', {'retval': {'type': sel32or64(b'{CGSize=ff}', b'{CGSize=dd}')}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'provideImageData:bytesPerRow:origin::size::userInfo:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^v', 'type_modifier': b'o', 'c_array_of_variable_length': True}, 3: {'type': sel32or64(b'L', b'Q')}, 4: {'type': sel32or64(b'L', b'Q')}, 5: {'type': sel32or64(b'L', b'Q')}, 6: {'type': sel32or64(b'L', b'Q')}, 7: {'type': sel32or64(b'L', b'Q')}, 8: {'type': b'@'}}})
    r(b'NSObject', b'region', {'retval': {'type': sel32or64(b'{CGRect={CGPoint=ff}{CGSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}})
    r(b'NSObject', b'repeatCount', {'required': True, 'retval': {'type': b'f'}})
    r(b'NSObject', b'repeatDuration', {'required': True, 'retval': {'type': b'd'}})
    r(b'NSObject', b'runActionForKey:object:arguments:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'setAutoreverses:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setBeginTime:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setDuration:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setFillMode:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setRepeatCount:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'f'}}})
    r(b'NSObject', b'setRepeatDuration:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setSpeed:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'f'}}})
    r(b'NSObject', b'setTimeOffset:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'speed', {'required': True, 'retval': {'type': b'f'}})
    r(b'NSObject', b'timeOffset', {'required': True, 'retval': {'type': b'd'}})
finally:
    objc._updatingMetadata(False)
protocols={'CAAnimationDelegate': objc.informal_protocol('CAAnimationDelegate', [objc.selector(None, b'animationDidStart:', b'v@:@', isRequired=False), objc.selector(None, b'animationDidStop:finished:', b'v@:@Z', isRequired=False)]), 'CALayerDelegate': objc.informal_protocol('CALayerDelegate', [objc.selector(None, b'drawLayer:inContext:', b'v@:@^{CGContext=}', isRequired=False), objc.selector(None, b'actionForLayer:forKey:', b'@@:@@', isRequired=False), objc.selector(None, b'displayLayer:', b'v@:@', isRequired=False), objc.selector(None, b'layoutSublayersOfLayer:', b'v@:@', isRequired=False)]), 'CIImageProvider': objc.informal_protocol('CIImageProvider', [objc.selector(None, b'provideImageData:bytesPerRow:origin::size::userInfo:', sel32or64(b'v@:^vLLLLL@', b'v@:^vQQQQQ@'), isRequired=False)]), 'CALayoutManager': objc.informal_protocol('CALayoutManager', [objc.selector(None, b'preferredSizeOfLayer:', sel32or64(b'{CGSize=ff}@:@', b'{CGSize=dd}@:@'), isRequired=False), objc.selector(None, b'layoutSublayersOfLayer:', b'v@:@', isRequired=False), objc.selector(None, b'invalidateLayoutOfLayer:', b'v@:@', isRequired=False)])}
expressions = {}

# END OF FILE
