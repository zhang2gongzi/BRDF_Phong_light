import numpy as np
import moderngl_window as mglw

class OrbitCamera(mglw.WindowConfig):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theta = np.radians(30)
        self.phi = np.radians(60)
        self.r = 5
        self.eye = None
        self.view_mat = None
        self.update_view()

    def mouse_drag_event(self, x: int, y: int, dx: int, dy: int):
        
        self.theta -= np.radians(dx*0.4)
        self.phi-=np.radians(dy*0.3)
        self.phi = np.clip(self.phi, np.radians(10), np.radians(170))
        
        self.update_view()
    
    def mouse_scroll_event(self, x_offset: float, y_offset: float):
        
        self.r -= y_offset*0.1
        self.r = np.clip(self.r, 1, 10)
        
        self.update_view()
    
    def mouse_release_event(self, x: int, y: int, button: int):
        return super().mouse_release_event(x, y, button)
    
    def update_view(self):
        x = self.r*np.sin(self.phi)*np.cos(self.theta)
        y = self.r*np.sin(self.phi)*np.sin(self.theta)
        z = self.r*np.cos(self.phi)
        self.eye = np.array([x, y, z], dtype='f4')
        target = np.array([0, 0, 0], dtype='f4')
        up = np.array([0, 0, 1], dtype='f4')
        
        self.view_mat = self.gen_look_at(self.eye, target, up)
    
    def gen_look_at(self, eye, target, up):
        forward = np.array(target - eye)/np.linalg.norm(target - eye)
        side = np.cross(forward, up)/np.linalg.norm(np.cross(forward, up))
        up = np.cross(side, forward)/np.linalg.norm(np.cross(side, forward))

        view = np.array((
                (side[0], up[0], -forward[0], 0.),
                (side[1], up[1], -forward[1], 0.),
                (side[2], up[2], -forward[2], 0.),
                (-np.dot(side, eye), -np.dot(up, eye), np.dot(forward, eye), 1.0)
            ), dtype='f4')
        return view