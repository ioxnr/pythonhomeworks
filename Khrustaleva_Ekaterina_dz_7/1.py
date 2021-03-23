import os

dir_name = 'my_project'


def make_directories(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


make_directories(dir_name)

dir_path_1 = os.path.join(dir_name, 'settings')
make_directories(dir_path_1)

dir_path_2 = os.path.join(dir_name, 'mainapp')
make_directories(dir_path_2)

dir_path_3 = os.path.join(dir_name, 'adminapp')
make_directories(dir_path_3)

dir_path_4 = os.path.join(dir_name, 'authapp')
make_directories(dir_path_4)
