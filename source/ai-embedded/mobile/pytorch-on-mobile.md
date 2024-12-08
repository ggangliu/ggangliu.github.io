# Pytorch on Mobile

PyTorch 1.7 supports the ability to run model inference on GPUs that support the Vulkan graphics and compute API.

1. How to save and import a custom model
   [Integrating Custom PyTorch Models Into an Android App](https://medium.com/mlearning-ai/integrating-custom-pytorch-models-into-an-android-app-a2cdfce14fe8)
2. How to override forward and backward
   [EXTENDING TORCHSCRIPT WITH CUSTOM C++ OPERATORS](https://pytorch.org/tutorials/advanced/torch_script_custom_ops.html)
3. How to use GPU on android device
   Rebuilding Pytorch source with Vulkan support, the default version is running on CPU

## Android

OS	Android 12, MIUI 13
CPU	Octa-core (4x2.85 GHz Cortex-A78 & 4x2.0 GHz Cortex-A55)
GPU	Mali-G610/G710

## PyTorch Mobile supports the following backends:

- CPU
- NNAPI (Android)
- CoreML (iOS)
- Metal GPU (iOS)
- Vulkan (Android)

### Vulkan Bankend

To use PyTorch with Vulkan backend, we need to build it from source with additional settings.
The main switch to include Vulkan backend is cmake option USE_VULKAN, that can be set by environment variable **USE_VULKAN**.

### [Vulkan SDK](https://pytorch.org/tutorials/prototype/vulkan_workflow.html)

Download VulkanSDK from https://vulkan.lunarg.com/sdk/home and set environment variable **VULKAN_SDK**

## Neural Networks API

https://github.com/android/ndk-samples/tree/main/nn-samples

## Pytorch API

<https://pytorch.org/javadoc/1.9.0/>

### Class LiteModuleLoader


## Reference

- [Added Inference Button](https://github.com/pytorch/workshops/tree/master/PTMobileWalkthruAndroid/app)
- [The example of using Vulkan backend](https://github.com/pytorch/pytorch/blob/main/android/test_app/app/src/main/java/org/pytorch/testapp/MainActivity.java#L133)