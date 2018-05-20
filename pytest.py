import src.client
import pytest

system = bootstrap_system()

def test_make_booking_empty_start():
	with pytest.raises(Exception) as err:
		empty_start = Location(pickup = None, 'Test')
		system.make_booking(system._customers[0], 1, system._cars[0], empty_start)

def test_make_booking_empty_finish():
	with pytest.raises(Exception) as err:
		empty_finish = Location('Test', dropoff = None)
		system.make_booking(system._customers[0], 1, system._cars[0], empty_finish)

def test_make_booking_empty_period():
	with pytest.raises(Exception) as err:
		test = Location('Test', 'Test')
		system.make_booking(system._customers[0], period = None, system._cars[0], test)

def test_make_booking_negative_period():
	with pytest.raises(Exception) as err:
		test = Location('Test', 'Test')
		system.make_booking(system._customers[0], -1, system._cars[0], test)

def test_correct_calculation_large_car();
		car = Large_Car('TestCar', 'TestModel', 999)
		assert car.get_fee(1) == 100
		assert car.get_fee(10) == (100 * 10) * 0.95

def test_correct_calculation_premium_car();
		car = Premium_Car('TestCar', 'TestModel', 999)
		assert car.get_fee(1) == 150 * 1.15
		assert car.get_fee(10) == (150 * 10) * 1.15
