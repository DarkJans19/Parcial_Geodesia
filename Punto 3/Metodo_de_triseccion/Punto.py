import math

class Punto:
    def __init__(self, x: float, y: float, angulo: float, direccion_x: str, direccion_y: str):
        self.x = x
        self.y = y
        self.angulo = angulo
        self.direccion_x = direccion_x.upper()  # Dirección puede ser N, S, E, W
        self.direccion_y = direccion_y.upper()  # Dirección puede ser N, S, E, W
        
    def ajustar_signo(self, valor: float, direccion: str) -> float:
        """Ajusta el signo según la dirección."""
        if direccion == 'S' or direccion == 'W':
            return -valor
        return valor
    
    def diferencia_x(self, b: 'Punto') -> float:
        # Ajustamos las coordenadas de acuerdo con la dirección
        diferencia_x = self.x - b.x
        return self.ajustar_signo(diferencia_x, self.direccion_x)
    
    def diferencia_y(self, b: 'Punto') -> float:
        # Ajustamos las coordenadas de acuerdo con la dirección
        diferencia_y = self.y - b.y
        return self.ajustar_signo(diferencia_y, self.direccion_y)
    
    def distancia(self, b: 'Punto'):
        diferencia_x = self.diferencia_x(b)
        print("diferencia_x:", diferencia_x)
        diferencia_y = self.diferencia_y(b)
        print("diferencia y:", diferencia_y)
        distancia = pow(diferencia_x, 2) + pow(diferencia_y, 2)
        return math.sqrt(distancia)
    
    def angulo(self, b: 'Punto', c: 'Punto'):
        # Diferencia C - A
        
        diferencia_x_c_a = c.diferencia_x(self)
        diferencia_y_c_a = c.diferencia_y(self)
        
        # Diferencia B - A
        
        diferencia_x_b_a = b.diferencia_x(self)
        diferencia_y_b_a = b.diferencia_y(self)

        # Diferencai C - B
        
        diferencia_x_c_b = c.diferencia_x(b)
        diferencia_y_c_b = c.diferencia_y(b)
        
        # Diferencia B - c
        diferencia_x_b_c = b.diferencia_x(c)
        diferencia_y_b_c = b.diferencia_y(c)
        
        # Ahora diferencia A - B
        
        diferencia_x_a_b = self.diferencia_x(b)
        diferencia_y_a_b = self.diferencia_y(b)
        
        # Por ultimo diferencia A - C
        
        diferencia_x_a_c = self.diferencia_x(c)
        diferencia_y_a_c = self.diferencia(c)
        
        # Calculamos el ángulo en radianes
        angulo_1 = math.atan(diferencia_x_c_a/diferencia_y_c_a) - math.atan(diferencia_x_b_a/diferencia_y_b_a)
        angulo_2 = math.atan(diferencia_x_a_b/diferencia_y_a_b) - math.atan(diferencia_x_c_b/diferencia_y_c_b)
        angulo_3 = math.atan(diferencia_x_b_c/diferencia_y_b_c) - math.atan(diferencia_x_a_c/diferencia_y_a_c)
        return math.degrees(angulo_1), math.degrees(angulo_2), math.degrees(angulo_3)
    
    def constantes(punto: 'Punto', angulo: float) -> float:
        cot_1 = 1/math.tan(math.radians(angulo))
        cot_2 = 1/math.tan(math.radians(punto.angulo)) 
        k = 1/(cot_1 - cot_2)
        return k
    
    def coordenadas(A, B, C, k1, k2, k3):
        suma_constantes = k1 + k2 + k3
        ep = ((k1 * A.x) + (k2 * B.x) + (k3 * C.x))/suma_constantes
        np = ((k1 * A.y) + (k2 * B.y) + (k3 * C.y))/suma_constantes
        return ep, np