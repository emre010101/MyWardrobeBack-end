# MyWardrobeBack-end
__Custom 3D Avatar Creator__

> This project allows users to create custom 3D avatars from their uploaded selfies. Users can also match their body shape and choose clothing for their avatars. 
The project uses Python, OpenCV, and Blender to create and modify 3D models.

## Features
- Face extraction from uploaded selfies
- Face texture creation and application to 3D avatars
- Body shape matching (version 2)
- Clothes selection and application to avatars (version 3)
- User wardrobe management

## Requirements
- Python 3.7+
- OpenCV
- Blender
- pygltflib

## Installation
1. Clone the repository:
_git clone https://github.com/emre010101/custom-3d-avatar-creator.git_

2. Change to the project directory:
_cd custom-3d-avatar-creator_

3. Create a virtual environment:
_python -m venv venv_

4. Activate the virtual environment:
- On Windows:
_venv\Scripts\activate_

- On Linux or macOS:
_source venv/bin/activate_

5. Install the required Python packages:
_pip install -r requirements.txt_

6. Install __Blender__ and ensure it's added to your system's PATH.

## Blender Python Script
<p align="center">
<img src="https://user-images.githubusercontent.com/118063573/236482619-f4ae6ce0-75e3-4937-9f25-803ce8aca572.png", height="250px">
</p>

## Usage
1. Run the application:
__python app/main.py__

2. Open your web browser and go to the URL shown in the terminal.

3. Register an account and log in.

4. Follow the steps in the application to create and customize your 3D avatar.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request. If you have any questions or issues, please open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
