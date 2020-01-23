import os, sys
import psycopg2
lib_path = os.path.abspath(os.path.join('package'))
sys.path.append(lib_path)
from tkinter import *
from tkinter import messagebox
from package.ConnectToPostgresql import connect
from package.DataForPostgresql import connectFrame
from package.AddData import addData
from package.menu import menu

dataConnect = connectFrame()
menu()

