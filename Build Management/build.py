# cars_project/build.py
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "cars_project"
default_task = "publish"

@init
def set_properties(project):
    project.depends_on("coverage")

    # Add other project settings if needed
    project.set_property("dir_source_main_python", "src/cars")
    project.set_property("dir_source_unittest_python", "tests")
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("coverage_threshold_warn", 70)
    project.set_property("coverage_branch_threshold_warn", 50)