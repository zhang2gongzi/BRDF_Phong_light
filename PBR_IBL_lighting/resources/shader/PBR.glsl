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

uniform vec3 lightPositions[4];
uniform vec3 lightColors[4];
uniform vec3 camPos;
uniform float ambientStrength;
uniform float diffuseStrength;
uniform float specularStrength;

void main() {
    vec3 result = vec3(0.0);

    vec3 norm = normalize(normal);
    vec3 viewDir = normalize(camPos - fragPos);

    for (int i = 0; i < 4; i++) {
        vec3 lightDir = normalize(lightPositions[i] - fragPos);
        float diff = max(dot(norm, lightDir), 0.0);
        vec3 diffuse = diffuseStrength * diff * albedo;
        result += diffuse * lightColors[i];

        vec3 reflectDir = reflect(-lightDir, norm);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
        vec3 specular = specularStrength * spec * vec3(1.0);
        result += specular * lightColors[i];
    }

    vec3 ambient = ambientStrength * albedo;
    result += ambient;

    FragColor = vec4(result, 1.0);
}