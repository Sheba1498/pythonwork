class Editor:
    def functionalities(self):
        self.funs=["createnewfile","execute","save"]
        return self.funs

class Pycham(Editor):
    def functionalities(self):
        funs=super().functionalities()
        funs.append(["debug","versioncontrol"])
        return funs

py=Pycham()
print(py.functionalities())