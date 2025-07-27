import pkg_resources

print("Installed pip packages in current virtual environment:\n")
for package in pkg_resources.working_set:
    print(f"{package.project_name}=={package.version}")
