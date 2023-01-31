#!/usr/bin/env python3

'''
    Implementacion ejemplo de servidor y servicio REST
'''


from src.client import DirectoryService

URI = "http://172.17.0.2:3302"

def main():
    '''Entry point'''

    directory=DirectoryService(URI, "uri_auth").get_root("admin")
    response=directory.new_directory("dirA")
    print(response)
    print(directory.self_info())
    directory.remove_directory("dirA")
    res3=directory.new_file("test.txt","/test.txt")
    res4=directory.list_files()

    directory.remove_file("test.txt")
    res5=directory.list_files()
    print(res3)
    print(res4)
    print(res5)

if __name__ == '__main__':
    main()