import tkinter as tk
from tkinter import messagebox

from click import command


def show_success():
    messagebox.showinfo("Success", "预约成功")
def show_fail():
    messagebox.showinfo("Error", "预约失败")

