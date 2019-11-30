from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='minicloudsky',
    author_email='minicloudsky@gmail.com',
    url='https://www.yawujia.cn',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': [
        'themes/*/*/*//*',
    ]},
    # include_package_data=True, #方法二: 配合MANIFEST.in文件
    install_requires=[
        'django~=1.11',
    ],
    extra_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[
        # 软件成熟度
        # 3 -Alpha 4 -beta 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # 指明项目的受众
        'Intended Audience :: Developers',
        'Topic  :: Software Development :: Libraries',
        # 选择项目的许可证(license)
        'License :: OSI Approved :: MIT License',
        # 指定项目需要的Python版本
        'Programming Language :: Python 3.6',
    ],

)
