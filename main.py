# # Приклад 2.1
# class A():
#     def __call__(self): return 'Student '
#
#
# class C(A):
#     def __call__(self): return 'Chloe '
#
#
# class B(A):
#     def __call__(self): return 'Bob '
#
#
# class P(A):
#     def __call__(self): return 'Piter '
#
#
# class D(B, C):
#     def __init__(self):
#         self.name = 'Denis'
#         print(A().__call__() + super().__call__() +
#               '(' + super(B, self).__call__() + ')' + ' like ' + self.name)
#
#
# class E(C, P, B):
#     def __init__(self):
#         self.name = 'Eelay'
#         print(A().__call__() + super().__call__() +
#               '(' + super(C, self).__call__() + super(P, self).__call__() + ')' + ' like' + self.name)
#
#
# class F(P, B):
#     def __init__(self):
#         self.name = 'Forth'
#         print(A().__call__() + super().__call__() +
#               '(' + super(P, self).__call__() + ')' + ' like ' + self.name)
#
#
# I1 = D(); I2 = E(); I3 = F()


# # Приклад 2.2 Множинне успадкування
# class Bird(object):
#     def fly(self):
#         print('I am flying.')
# class Horse(object):
#     def run(self):
#         print('I am running.')
# class Pegasus(Horse, Bird): pass
# def main():
#     bird = Bird()
#     horse = Horse()
#     pegasus = Pegasus()
#     bird.fly()
#     # bird.run() # ошибка
#     print()
#     # horse.fly() # ошибка
#     horse.run(); print()
#     pegasus.fly(); pegasus.run()
# if __name__ == '__main__': main()


# # Приклад 2.3 Порядок дозволу методів при ромбоподібному множинному успадкуванні
# class A(object):
#     def method(self):
#         print('A method')
# class B(A): pass
# class C(A):
#     def method(self):
#         print('C method')
# class D(B, C): pass
# obj = D()
# obj.method() # 'C method'

# # Приклад 2.4
# class A:
#     def method(self):
#         print('A method')
# class B(A): pass
# class C(A):
#     def method(self):
#         print('C method')
# class D(B, C): pass
# obj = D(); obj.method()

# # Приклад 2.5 (перший спосіб)
# class Base:
#     attr = 'Base attribute'
#     def method(self):
#         print('Base method, current class is', self.__class__.__name__)
# class Child(Base):
#     attr = 'Redefined attribute'
#     @staticmethod
#     def get_superclass_attr():
#         return Base.attr # отримання атрибуту класа Base
#     def method(self): # перевизначення методу
#         Base.method(self)  # вызов метода суперкласса
#         print('Child method, current class is', self.__class__.__name__)
# def main():
#     print('Base:'); print(Base.attr)
#     base_instance = Base(); base_instance.method()
#     print(); print('Child:'); print(Child.attr)
#     print(Child.get_superclass_attr())
#     child_instance = Child()
#     child_instance.method()
# if __name__ == '__main__': main()


# # Приклад 2.5 (другий спосіб)
# class Base(object):
#     attr = 'Base attribute'
#     def method(self):
#         print('Base method, current class is', self.__class__.__name__)
# class Child(Base):
#     attr = 'Redefined attribute'
#     def get_superclass_attr(self):
#         return super().attr # отримання атрибуту класа Base
#     def method(self): # перевизначення методу
#         super().method() # виклик метода суперкласу
#         print('Child method, current class is', self.__class__.__name__)
# def main():
#     print('Base:'); print(Base.attr)
#     base_instance = Base()
#     base_instance.method(); print()
#     print('Child:'); print(Child.attr)
#     child_instance = Child()
#     print(child_instance.get_superclass_attr())
#     child_instance.method()
#     print()
# # super можна викликати де завгодно, навіть за межами класу
#     super(Child, child_instance).method()
# if __name__ == '__main__': main()

# # Приклад 2.6 Використання super при множинному успадкуванні
# class Animal(object):
#     def __init__(self):
#         self.can_fly = False
#         self.can_run = False
#     def print_abilities(self):
#         print(self.__class__.__name__)
#         print('Can fly:', self.can_fly)
#         print('Can run:', self.can_run); print()
# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_fly = True
# class Horse(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_run=True
# class Pegasus(Horse, Bird): pass
# def main():
#     bird = Bird()
#     bird.print_abilities()
#     horse = Horse()
#     horse.print_abilities()
#     pegasus = Pegasus()
#     pegasus.print_abilities()
# if __name__ == '__main__': main()

# # Приклад 2.7
# def gen_init(cls):
#     """ Декоратор gen_init:
# :param cls: клас, який підлягає модифікації
# :return: клас із доданим конструктором """
#     def init(self):
#         print('Entered', cls.__name__, "constructor")
#         super(cls, self).__init__()
#         print('Quit', cls.__name__, "constructor")
#     cls.__init__ = init
#     return cls
# @gen_init
# class A(object): pass
# @gen_init
# class B(object): pass
# @gen_init
# class C(A, B): pass
# @gen_init
# class D(C, B): pass
# @gen_init
# class E(D): pass
# print(E.__mro__); obj = E()

# # Приклад 2.8 Функція isinstance (obj, cls) перевіряє, чи є obj екземпляром класу cls або
# # класу, який є спадкоємцем класу cls
# print(isinstance(8, int)) # True
# print(isinstance('str', int)) # False
# print(isinstance(True, bool)) # True
# print(isinstance(True, int)) # True, тому що bool - підклас int
# print(isinstance('a string', object)) # True, все є об‘єктами
# print(isinstance(None, object)) # True, навіть None
# print(isinstance(False, str)) # False
# print(isinstance(int, type))
# # True, будь-який клас – об‘єкт-екземпляр метакласу type
# print(isinstance(42, type)) # False, 42 – це не тип даних

# # Приклад 2.9 Функція issubclass(cls, base) перевіряє, чи є класс cls спадкоємцемкласу base.
# print(issubclass(bool, int)) # True
# print(issubclass(float, int)) # False
# print(issubclass(int, float)) # False
# print(issubclass(complex, type)) # False
# print(issubclass(complex, object))
# # True, всѐ наследуется от object
# class Base(object): pass
# class Child(object): pass
# print(issubclass(Child, Base)) # True
# print(issubclass(Base, object)) # True
# print(issubclass(Child, object)) # True по транзитивності








# Індивідуальне завдання
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def send_order(self):
        return f"{self.name} відправив замовлення."

    def receive_order(self):
        return f"{self.name} отримав замовлення."


class Order(Customer):
    def __init__(self, data, number, name, address):
        super().__init__(name, address)
        self.data = data
        self.number = number
        self.fruits_and_vegetables = ["яблука", "банани", "апельсини", "мандарини", "груші", "виноград", "ківі", "ананаси",
                             "манго", "персики", "помідори", "огірки", "перець", "картопля", "морква", "цибуля",
                             "часник", "капуста", "буряк", "кукурудза"]

    def confirm(self):
        for el in self.data:
            if el in self.fruits_and_vegetables:
                return f"Замовлення №{self.number}: {self.data} для {self.name}. Підтверджено!"
            else:
                return f"Замовлення №{self.number} для {self.name}. Не підтверджено! " \
                       f"Таких товарів не має в магазині!"

    def close(self):
        return f"Замовлення №{self.number} закрито (зроблене)."


class SpecialOrder(Order):
    def __init__(self, data, number, name, address):
        super().__init__(data, number, name, address)
        self.__private_client = None

    def confirm(self):
        return "Спеціальне " + super().confirm()

    def close(self):
        return "Спеціальне " + super().close()

    def dispatch(self):
        return f"Спеціальне замовлення №{self.number} для {self.name} за адресою: {self.address} відправлено."


class NormalOrder(Order):
    def __init__(self, data, number, name, address):
        super().__init__(data, number, name, address)

    def confirm(self):
        return "Звичайне " + super().confirm()

    def close(self):
        return "Звичайне " + super().close()

    def dispatch(self):
        return f"Звичайне замовлення №{self.number} для {self.name} за адресою: {self.address} відправлено"

    def receive(self):
        return f"{self.name} отримав замовлення."


print("==================================================================================")
customer1 = Customer("John", "12 Main St")
spec_order1 = SpecialOrder(["яблука", "морква"], "1", "John", "12 Main St")
print(customer1.send_order())
print(spec_order1.confirm())
print(spec_order1.close())
print(spec_order1.dispatch())
print(customer1.receive_order())
print("==================================================================================")

customer2 = Customer("Alex", "15 Cherry St")
norm_order1 = NormalOrder(["груші", "манго"], "2", "Alex", "15 Cherry St")
print(customer2.send_order())
print(norm_order1.confirm())
print(norm_order1.close())
print(norm_order1.dispatch())
print(customer2.receive_order())
print("==================================================================================")

customer3 = Customer("Anna", "25 Main St")
norm_order2 = NormalOrder(["авокадо"], "3", "Anna", "25 Main St")
print(customer3.send_order())
print(norm_order2.confirm())
print(norm_order2.close())
print(norm_order2.dispatch())
print(norm_order2.receive())
print("==================================================================================")





