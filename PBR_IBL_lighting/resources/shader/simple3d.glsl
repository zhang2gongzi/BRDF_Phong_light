#type vertex
#version 460

layout(location = 0) in vec3 in_position;
layout(location = 1) in vec3 in_normal;
layout(location = 2) in vec3 in_albedo;
layout(location = 3) in float in_metallness;
layout(location = 4) in float in_roughness;
layout(location = 5) in float in_ao;

out vec3 fragPos;
out vec3 normal;
out vec3 albedo;
out float metallness;
out float roughness;
out float ao;

uniform mat4 mvp;

void main() {
    fragPos = in_position;
    normal = in_normal;
    albedo = in_albedo;
    metallness = in_metallness;
    roughness = in_roughness;
    ao = in_ao;

    gl_Position = mvp * vec4(in_position, 1.0);
}

#type fragment
#version 460

in vec3 fragPos;
in vec3 normal;
in vec3 albedo;
in float metallness;
in float roughness;
in float ao;

out vec4 FragColor;

void main() {
    FragColor = vec4(albedo, 1.0);
}