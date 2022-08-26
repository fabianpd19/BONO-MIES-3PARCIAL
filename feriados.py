import datetime
import requests
import os
import json
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR
from holidays.constants import JAN, MAY, AUG, OCT, NOV, DEC, JUN, FEB, MAR, APR, JUL
from holidays.holiday_base import HolidayBase

class FeriadoEcuador(HolidayBase):
    """
    Una clase para representar un feriado en Ecuador por provincia (FiestaEcuador)
    Su objetivo es determinar si un
    fecha específica es unas vacaciones lo más rápido y flexible posible.
    https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (Hereda la clase HelidayBase )
    ----------
    prov: str
        código de provincia según ISO3166-2
    Metodos
    -------
    __init__(self, lamina, fecha, tiempo, enLinea=False):
        Construye todos los atributos necesarios para el objeto FiestaEcuador.
    _populate(self, anio):
        Retornar si una fecha es festiva o no
    """     
    # Códigos ISO 3166-2 para las principales subdivisiones,
    # provincias llamadas
    # https://es.wikipedia.org/wiki/ISO_3166-2:EC
    PROVINCES = ["EC-P"]  # TODO añadir más provincias

    def __init__(self, **kwargs):
        """
         Construye todos los atributos necesarios para el objeto HolidayEcuador.
        """         
        self.country = "ECU"
        self.prov = kwargs.pop("prov", "ON")
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):                             #
        """
        Comprueba si una fecha es festiva o no 
        Parámetros 
        ----------
             year : str año de una fecha Devuelve 
         ------
             Devuelve verdadero si una fecha es festiva de lo contrario false
        """                    
        # New Year's Day 
        self[datetime.date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        
        # Christmas
        self[datetime.date(year, DEC, 25)] = "Navidad"

        #carnaval lunes y martes
        self[datetime.date(year, FEB, 28)] = "Carnaval [carnaval lunes]" 
        self[datetime.date(year, MAR, 1)] = "Carnaval [carnaval martes]"

        #Pascua
        self[datetime.date(year, APR, 17)] = "Dia de pascua "
        

        #semana santa
        self[datetime.date(year, APR, 2)] = "Semana Santa "
        self[datetime.date(year, APR, 3)] = "Semana Santa "
        self[datetime.date(year, APR, 4)] = "Semana Santa "
        self[datetime.date(year, APR, 5)] = "Semana Santa "
        self[datetime.date(year, APR, 6)] = "Semana Santa "
        self[datetime.date(year, APR, 7)] = "Semana Santa "
        self[datetime.date(year, APR, 8)] = "Semana Santa "

        #Dia del trabajo
        self[datetime.date(year, MAY, 1)] = "Dia del trabajo "
        self[datetime.date(year, MAY, 2)] = "Dia del trabajo "

        #Batalla de pichincha
        self[datetime.date(year, MAY, 23)] = "Baalla Pichincha"

        #Dia de simon Bolivar
        self[datetime.date(year, JUL, 25)] = "Dia simon Bolivar"

        #Dia de independencia
        self[datetime.date(year, AUG, 10)] = "Dia de independencia"

        #Dia de muertos
        self[datetime.date(year, NOV, 2)] = "Dia de muertos"

        #cantonizacion santo domingo
        self[datetime.date(year, JUL, 3)] = "Cantonizacion santo domingo"

        #provincializacion de santo domingo
        self[datetime.date(year, OCT, 6)] = "Provincializacion de sano domingo"
    
class feriadosEcuador:                
    '''
    Una clase la cual va a refleijar los dias de feriados . '''
    
    #Dias de la semana 
    __days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

    # Restricciones de las fechas de feriados
    __restrictions = {
            "Monday": [1, 2],
            "Tuesday": [3, 4],
            "Wednesday": [5, 6],
            "Thursday": [7, 8],
            "Friday": [9, 0],
            "Saturday": [],
            "Sunday": []}

    def __init__(self, date, online=False):                
        """
         Construye todos los atributos necesarios para el objeto PicoPlaca.
        
         Parámetros
         ----------
            fecha: str
                 Fecha en la que el vehículo pretende transitar
                 Sigue el formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.  
            en línea: booleano, opcional
                 si en línea == Verdadero, se usará la API de días festivos abstractos (el valor predeterminado es Falso)           
        """                
        self.date = date
        self.online = online
        
        
    @property
    def date(self):
        """Gets the date attribute value"""
        return self._date


    @date.setter
    def date(self, value):
        """
        Sets the date attribute value
        Parameters
        ----------
        value : str
        
        Raises
        ------
        ValueError
            If value string is not formated as YYYY-MM-DD (e.g.: 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'The date must be in the following format: YYYY-MM-DD (e.g.: 2021-04-02)') from None
        self._date = value

    def __is_holiday(self, date, online):       
        """
         Comprueba si la fecha (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador
         si en línea == Verdadero, utilizará una API REST, 
         de lo contrario, generará los días festivos del año examinado
        
         Parámetros
         ----------
         fecha: calle
             Está siguiendo el formato ISO 8601 AAAA-MM-DD: 
             por ejemplo, 2020-04-22
         en línea: booleano, opcional
             si en línea == Verdadero, se utilizará la API de días festivos abstractos
         Devoluciones
         -------
         Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
          de lo contrario, Falso
        """            
        y, m, d = date.split('-')

        if online:
            # API de vacaciones abstractapi, versión gratuita: 1000 solicitudes por mes
            # 1 solicitud por segundo
            # recuperar la clave API de la variable de entorno
            key = os.environ.get('HOLIDAYS_API_KEY')
            response = requests.get(
                "https://holidays.abstractapi.com/v1/?api_key={}&country=EC&year={}&month={}&day={}".format(key, y, m, d))
            if (response.status_code == 401):
                # Esto significa que falta una clave API
                raise requests.HTTPError(
                    'Falta la clave API. Guarde su clave en la variable de entorno HOLIDAYS API_KEY')
            if response.content == b'[]':  # si no hay vacaciones, obtenemos una matriz vacía
                return False
            # Arreglar el Jueves Santo incorrectamente denotado como feriado
            if json.loads(response.text[1:-1])['name'] == 'Maundy Thursday':
                return False
            return True
        else:
            ecu_holidays = FeriadoEcuador(prov='EC-SD')
            return date in ecu_holidays

    def predict(self):         
        """
         -------
         
         Verdadero si fecha  con online
           Es dia festivo
         en la fecha especificadas, de lo contrario Falso
        """
        # Check if date is a holiday
        if self.__is_holiday(self.date, self.online):       
            return True
        return False        