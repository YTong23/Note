import subprocess
import os
import random

# 生成 5x5 的随机整数列表（范围 0-100）


# 打印结果



# 设置你的 Git 仓库路径
repo_path = "."  # 请修改为你的本地仓库路径
commit_message = "自动提交更新"

def git_push():
    try:
        with open(os.devnull, "w") as devnull:
            subprocess.run(["git", "add", "."], stdout=devnull, stderr=devnull, check=True)
            subprocess.run(["git", "commit", "-m", commit_message], stdout=devnull, stderr=devnull, check=True)
            subprocess.run(["git", "push", "origin", "main"], stdout=devnull, stderr=devnull, check=True)

    except subprocess.CalledProcessError as e:
        print()

if __name__ == "__main__":
    a = int(input("input w: "))
    b = int(input("input b: "))
    git_push()
    random_list = [[random.randint(0, 100) for _ in range(a)] for _ in range(b)]
    for row in random_list:
        print(row)
