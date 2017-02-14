
####################### Clase ######################
class Estudiante:
    #Atributos de la clase
    _matricula = ""
    _ci = ""
    _nombre = ""
    _carrera = ""
    _facultad = ""

#################### Constructor ####################
    def __init__(self, matricula, ci, nombre, carrera, facultad):
        self._matricula = matricula
        self._ci = ci
        self._nombre = nombre
        self._carrera = carrera
        self._facultad = facultad

####################### Cadena #######################
    def __str__(self):
        return ("\n\t\t\tMATRICULA:\t\t\t\t"+self._matricula.zfill(9)
                +"\n\t\t\tC.I:\t\t\t\t\t"+self._ci.zfill(10)
                +"\n\t\t\tNOMBRE:\t\t\t\t\t"+self._nombre.upper()
                +"\n\t\t\tCARRERA:\t\t\t\t"+self._carrera.upper()
                +"\n\t\t\tFACULTAD:\t\t\t\t"+self._facultad.upper()+"\n")

################# Metodos de la clase #################
    def set_matricula(self,matricula):
        self._matricula = matricula
    def get_matricula(self,matricula):
        return self._matricula
    def set_ci(self,ci):
        self._ci = ci
    def get_ci(self):
        return self._ci
    def set_nombre(self,nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_carrera(self,carrera):
        self._carrera = carrera
    def get_carrera(self):
        return self._carrera
    def set_facultad(self,facultad):
        self._facultad = facultad
    def get_facultad(self):
        return self._facultad
