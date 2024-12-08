# TensorFlow Lite

https://developer.android.com/codelabs/digit-classifier-tflite?hl=en#6

[自定义算子](https://www.tensorflow.org/lite/guide/ops_custom?hl=zh-cn)

## Embedded

[TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers/overview?hl=zh-cn)

### 模型训练

OCR

### 开发工作流程

- 创建或获取TensorFlow模型
- 将模型转换为TensorFlow Lite FlatBuffer
  使用[TensorFlowLite转换器](https://www.tensorflow.org/lite/microcontrollers/build_convert?hl=zh-cn#%E8%BD%AC%E6%8D%A2%E6%A8%A1%E5%9E%8B)来将模型转换为标准 TensorFlow Lite 格式
- 将 FlatBuffer 转换为 C byte 数组
  模型保存在只读程序存储器中，并以简单的 C 文件的形式提供。标准工具可用于[将FlatBuffer转换为C数组](https://www.tensorflow.org/lite/microcontrollers/build_convert?hl=zh-cn#%E8%BD%AC%E6%8D%A2%E4%B8%BA_C_%E6%95%B0%E7%BB%84)。
- 集成TensorFlow Lite for Microcontrollers的C++库
  编写微控制器代码以使用[C++库](https://www.tensorflow.org/lite/microcontrollers/library?hl=zh-cn)执行推断。
  <https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro>
- 部署到您的设备

### 设备

["Blue Pill" STM32F103 兼容开发板](https://github.com/google/stm32_bare_lib)

<https://github.com/tensorflow/tflite-micro/tree/main>
<https://github.com/google/flatbuffers>

This example illustrates a way of personalizing a TFLite model on-device without sending any data to the server.

<https://github.com/tensorflow/examples/tree/master/lite/examples/model_personalization>