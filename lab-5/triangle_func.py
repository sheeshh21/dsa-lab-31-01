class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):

    # Проверка корректности сторон
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise IncorrectTriangleSides("Стороны должны быть числами")
    
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
    
    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника")
    
    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"