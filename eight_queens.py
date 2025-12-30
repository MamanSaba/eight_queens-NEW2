#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اسکریپت حل مسئله هشت وزیر
هر بار اجرا یک جواب تصادفی نمایش می‌دهد
"""

import random
import sys
import io

# تنظیم encoding برای ویندوز
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def is_safe(board, row, col):
    """بررسی می‌کند که آیا قرار دادن وزیر در موقعیت (row, col) امن است"""
    # بررسی ستون
    for i in range(row):
        if board[i] == col:
            return False
    
    # بررسی قطر اصلی (از بالا چپ به پایین راست)
    for i in range(row):
        if board[i] - i == col - row:
            return False
    
    # بررسی قطر فرعی (از بالا راست به پایین چپ)
    for i in range(row):
        if board[i] + i == col + row:
            return False
    
    return True


def solve_queens_random(board, row=0, max_solutions=1000):
    """حل مسئله با استفاده از الگوریتم تصادفی"""
    if row == 8:
        return True
     
    # لیست ستون‌های ممکن را به صورت تصادفی مرتب می‌کنیم
    cols = list(range(8))
    random.shuffle(cols)
    
    for col in cols:
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens_random(board, row + 1):
                return True
            board[row] = -1
    
    return False


def print_board(board):
    """نمایش صفحه شطرنج با وزیرها"""
    print("\n" + "="*35)
    print("  جواب تصادفی مسئله هشت وزیر")
    print("="*35 + "\n")
    
    # نمایش با شماره ستون
    print("   ", end="")
    for i in range(8):
        print(f" {i+1} ", end="")
    print("\n")
    
    # نمایش صفحه
    for row in range(8):
        print(f" {row+1} ", end="")
        for col in range(8):
            if board[row] == col:
                print(" ♕ ", end="")  # نماد وزیر
            else:
                # رنگ‌بندی صفحه شطرنج
                if (row + col) % 2 == 0:
                    print(" ▢ ", end="")
                else:
                    print(" ▦ ", end="")
        print()
    
    print("\n" + "="*35)
    print("موقعیت وزیرها (ردیف, ستون):")
    for row in range(8):
        print(f"  وزیر {row+1}: ردیف {row+1}, ستون {board[row]+1}")
    print("="*35 + "\n")


def main():
    """تابع اصلی"""
    # مقداردهی اولیه
    board = [-1] * 8
    
    # حل مسئله
    if solve_queens_random(board):
        print_board(board)
    else:
        print("خطا: نتوانست جواب پیدا کند!")
        sys.exit(1)


if __name__ == "__main__":
    main()

