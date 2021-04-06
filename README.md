# Phone-Book
Puhelinluettelo / A Phone Book Application

**********************************************************************
Tämä sovellus on osa Helsingin Yliopiston ohjelmoinnin MOOC - kurssia.
**********************************************************************

Separation of concerns -periaatetta noudatellen koodi tulee jakaa osiin, joista kukin käsittelee omaa asiaansa. Olio-ohjelmoinnin piirissä tätä periaatetta ilmentää niin sanottu yhden vastuun (single responsibility) -periaate. Eli yksittäisen luokan olioiden tulisi olla vastuussa yhdestä reaalimaailman ilmiöstä.

Puhelinluettelossa tälläisiä olisivat esimerkiksi: [henkilö, nimi, puhelinnumero ja puhelinluettelo]

Näistä henkilö voisi olla oma luokkansa, jonka vastuulla on sitoa yhteen tietty nimi ja siihen liittyvät puhelinnumerot.
Puhelinluettelo itsessään voisi olla luokka, jonka vastuulla on hallinnoida henkilöitä.

Nämä kaksi luokkaa muodostavat sovelluksen logiikan.
Sovelluslogiikan muodostavien luokkien lisäksi ohjelmalla on luokka käyttöliittymää varten.

Puhelinluettelon tietojen käsittely on selkeästi oma vastuunsa, joten siihen on myös luokkaansa.


****************************************************************************************
This application is part of the programming MOOC - course at the University of Helsinki.
****************************************************************************************

Following the principle of Separation of concerns, the code should be divided into sections, each dealing with its own case. In object-oriented programming, this principle is embodied in the single responsibility principle. That is, objects in a single class should be responsible for one real-world phenomenon.

The phonebook would include, for example: [person, name, phone number, and phonebook]

Of these, a person could be in a class of their own, responsible for tying together a particular name and associated phone numbers.
The phone book itself could be a class responsible for managing persons.

These two classes form the logic of the application.
In addition to the classes that make up the application logic, the program has a class for the user interface.

The processing of phone book data is clearly its own responsibility, so it also has a class to it.