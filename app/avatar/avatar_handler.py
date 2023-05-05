from pygltflib import GLTF2

class AvatarHandler:
    def __init__(self, gltf_model_path):
        self.gltf_model_path = gltf_model_path

    def apply_face_texture(self, face_texture_path):
        gltf = GLTF2.load(self.gltf_model_path)

        # Identify the face texture in the GLTF model (assuming it's the first texture)
        face_texture = gltf.textures[0]

        # Create a new image and set its URI to the new face texture path
        new_image = gltf.images[face_texture.source]
        new_image.uri = face_texture_path

        # Update the image reference in the face texture
        face_texture.source = len(gltf.images)  # The new image index will be at the end of the list
        gltf.images.append(new_image)

        # Save the modified GLTF model
        gltf.save("path/to/your/modified_gltf_model.gltf")
