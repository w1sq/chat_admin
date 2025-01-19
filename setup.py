from setuptools import setup, find_packages

setup(
    name="chat_admin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["aiogram==3.17"],
    entry_points={"console_scripts": ["chat_admin=src.bot:main"]},
    author="Kokorev Artem",
    author_email="artem.kokorev2005@yandex.ru",
    description="Bot for filtering messages in chats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/w1sq/chat_admin",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
