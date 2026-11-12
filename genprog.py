from typing import TypeVar, Generic
T = TypeVar("T")  # Global (Typevariabel)


class Lager(Generic[T]):

    totalt_antal_objekt = 0  # Klassvariabel

    def __init__(self, lager_namn: str) -> None:  # self, lager_namn: Lokala (parametrar)
        self.lager_namn = lager_namn  # Instansvariabel (publik)
        self._produkt: list[T] = []  # Instansvariabel (skyddad)

    def lägg_till(self, produkt: T) -> None:  # self, produkt: Lokala (parametrar)
        self._produkt.append(produkt)

        Lager.totalt_antal_objekt += 1

    def hämta(self) -> list[T]:  # self: Lokal (parameter)
        return list(self._produkt)

    def inventering(self) -> str:  # self: Lokal (parameter)
        # Enclosing (lokal i inventering samt nås av formatering)
        status: str = "lagerstatus"

        def formatering() -> str:

            prefix: str = ">>>"  # Lokal

            return f"{prefix} {self.hämta()} {status}: {len(self._produkt)} st"

        return formatering()


lager1 = Lager("yesyes")  # Global
lager1.lägg_till("Äpple")
lager1.lägg_till("Bannan")
lager1.lägg_till("Päron")

print(lager1.totalt_antal_objekt)
print(lager1.inventering())


# i. En klassvariabel lever lika länge som programmet eller klassen medan en lokal variabel endast lever under tiden den specifika metoden lever.
# ii. Anledningen till varför inre (nästlade) funktionen inte kan nå variablar som finns i en annan metod i samma klass beror på att deras lokala räkvid aldrig överlappar varandra eftersom de två olika metoderna har två helt olika lokala räkvidar som aldrig kommer att överlappa varandra i LEGB-kedjan.
