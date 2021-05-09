from setuptools import setup, find_packages
 
setup(
    name = 'ljpypi_test', 		                      # 필수
		version = '0.1.0',		                  # 필수
		packages = find_packages(exclude = []),	  # 필수
    description="uploading python package",
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    author="Lee Jung",
    author_email="lj8763@naver.com",
    keywords=["pypi"],
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)