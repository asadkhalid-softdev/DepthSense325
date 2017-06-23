from distutils.core import setup, Extension

module = Extension('DepthSense',
        include_dirs = ['/usr/local/include', '/opt/softkinetic/DepthSenseSDK/include'],
        libraries = ['DepthSensePlugins', 'DepthSense', 'python2.7', 'turbojpeg'],
        library_dirs = ['/usr/local/lib', '/opt/softkinetic/DepthSenseSDK/lib'],
        sources = ['grabber.cxx'])

setup (name = 'DepthSense',
        version = '1.0',
        description = 'Python Wrapper for the DepthSense SDK',
        long_description = '''The Python DepthSense SDK wrapper allows basic i
        interaction with the DepthSense camera.''',
        ext_modules = [module])
