# Fasternix Stratalorn -  Python module/library for saving the list of translators of a given Transifex project into a JSON file.
# Copyright (C) 2017 Nissar Chababy <contact at funilrys dot com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Original Version: https://github.com/funilrys/Fasternix-Stratalorn

from distutils.core import setup

setup(
    name='fasternix_stratalorn',
    version="1.1.1",
    description='Python module/library for saving the list of translators of a given Transifex project into a JSON file.',
    long_description=open('README').read(),
    author='funilrys',
    author_email='contact@funilrys.com',
    license='MIT https://opensource.org/licenses/MIT',
    url='https://github.com/funilrys/Fasternix-Stratalorn',
    platforms=['any'],
    packages=['fasternix_stratalorn'],
    keywords=[
        'Python',
        'JSON',
        'transifex',
        'translator',
        'translators'],
    classifiers=[
        'Environment :: Console',
        'Topic :: Internet',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''
