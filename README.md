# BRDF_Phong_light
本次实验为计算机图形学实验四内容，完成球体的Phong光照模型。实现程序用法通过动态的调节 Phong 模型中的各种参数并观察其对最重效果的影响，可以直观的看到环境光强、理想漫反射光强和镜面反射光对最终结果的影响，进而更加直观的理解该模型中各个成分的作用
光照模型是真实感图形渲染的基础，从 1967 年 Wylie 等人第一次在显示物体的时候加进光照效果后，该领域迅速的发展。简单的光照模型模拟物体表面对光的反射作用，它只考虑物体对直接光照的反射作用，而物体间的反射光只用环境光统一表示。Phong 模型就是这样一种模型。 Phong 光照模型可以表述为：由物体表面上一点 P 反射到视点的光强 I 为环境光的反射光强Ie、理想漫反射光强Id和镜面反射光Is的总和，即：<img width="400" alt="1729764951965" src="https://github.com/user-attachments/assets/da34a586-4055-4d86-a087-6426186369ec">     
This experiment is part of Computer Graphics Experiment 4, which aims to complete the Phong lighting model of a sphere. By dynamically adjusting various parameters in the Phong model and observing their impact on the heaviest effect, program usage can be implemented to intuitively see the effects of ambient light intensity, ideal diffuse reflection light intensity, and specular reflection light on the final result, thereby gaining a more intuitive understanding of the roles of each component in the model
The lighting model is the foundation of realistic graphic rendering, and since Wylie et al. first added lighting effects when displaying objects in 1967, this field has rapidly developed. A simple lighting model simulates the reflection of light on the surface of an object, which only considers the reflection of direct light by the object, while the reflection of light between objects is uniformly represented by ambient light. The Phong model is such a model. The Phong lighting model can be expressed as: the light intensity I reflected from a point P on the surface of an object to the viewpoint is the sum of the reflected light intensity Ie of ambient light, the ideal diffuse reflection light intensity Id, and the specular reflection light Is, that is:
