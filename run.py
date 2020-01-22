import os, sys
import psycopg2
lib_path = os.path.abspath(os.path.join('function'))
sys.path.append(lib_path)
from tkinter import *
from tkinter import messagebox
from function.ConnectToPostgresql import connect
from function.DataForPostgresql import connectFrame

connectFrame()
