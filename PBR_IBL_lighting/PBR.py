import moderngl_window as mglw
import moderngl as mgl
import numpy as np
from camera import OrbitCamera
from moderngl_window.geometry import sphere, cube
from pyrr import Matrix44 as m44
import os


class MainWin(OrbitCamera):
    title = "PBR"
    window_size = (1024, 512)
    gl_version = (4, 6, 0)
    aspect_ratio = window_size[0] / window_size[1]
    resource_dir = 'resources/'  # 确保这是正确的路径

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.N_inst = 1  # 只渲染一个球体
        self.simple3d = self.load_program("shader/simple3d.glsl")
        self.pbr_prog = self.load_program("shader/PBR.glsl")

        self.proj_mat = m44.perspective_projection(40, self.aspect_ratio, 0.1, 100)
        self.sph = sphere(0.4)

        # 只有一个球体的位置
        self.pos = np.array([
            [0, 0, 0]
        ], dtype='f4')

        # 只有一个球体的颜色
        self.sph_col = np.array([
            [0.00, 0.33, 1.00]
        ], dtype='f4')

        # 只有一个球体的材质属性
        self.materials = np.array([
            [0.00, 0.33, 1.00, 0.0, 0.1, 0.01]
        ], dtype='f4')

        self.sph.buffer(self.pos, "3f/i", "in_offset")
        self.sph.buffer(self.materials, "3f f f f/i", ["in_albedo", "in_metallness", "in_roughness", "in_ao"])

        self.light_pos = np.array([
            [2, 2, 2],
            [-2, 2, 2],
            [2, -2, 2],
            [2, 2, -2],
        ], dtype='f4')

        self.light_col = np.array([
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.]
        ], dtype='f4')

        # 光照参数
        self.ambient_strength = 0.1  # 环境光强
        self.diffuse_strength = 0.5  # 理想漫反射光强
        self.specular_strength = 0.8  # 镜面反射光强

        self.ctx.enable(mgl.DEPTH_TEST)

    def render(self, t, dt):
        self.ctx.clear()

        mvp = self.proj_mat * self.view_mat
        self.pbr_prog["mvp"].write(mvp.astype('f4'))
        self.pbr_prog["lightPositions"].write(self.light_pos * 2)
        self.pbr_prog["camPos"].write(self.eye)
        self.pbr_prog["lightColors"].write(self.light_col)

        # 传递光照参数
        self.pbr_prog["ambientStrength"].value = self.ambient_strength
        self.pbr_prog["diffuseStrength"].value = self.diffuse_strength
        self.pbr_prog["specularStrength"].value = self.specular_strength

        self.sph.render(self.pbr_prog, instances=self.N_inst)

    def load_program(self, relative_path):
        # 获取脚本文件的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建绝对路径
        abs_path = os.path.join(script_dir, 'resources', relative_path)
        print(f"Loading shader from: {abs_path}")

        # 确保使用 UTF-8 编码加载文件
        with open(abs_path, 'r', encoding='utf-8') as file:
            source = file.read()

        # 分离顶点着色器和片段着色器
        parts = source.split('#type ')
        vertex_shader = None
        fragment_shader = None

        for part in parts:
            if part.startswith('vertex'):
                vertex_shader = part.split('\n', 1)[1]
            elif part.startswith('fragment'):
                fragment_shader = part.split('\n', 1)[1]

        if vertex_shader is None or fragment_shader is None:
            raise ValueError(f"Shader file {abs_path} is missing vertex or fragment shader section.")

        # 创建着色器程序
        prog = self.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader
        )
        return prog


MainWin.run()