from jmms.calculadora import  Calculadora

def test_mas():
    cal = Calculadora()
    assert cal.suma(1 , 3 ) == 4


def test_resta():
    cal = Calculadora()
    assert cal.resta(3 , 1 ) == 2


def test_por():
    cal = Calculadora()
    assert cal.por(3 , 1 ) == 3
