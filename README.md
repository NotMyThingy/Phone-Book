# Phone-Book
Puhelinluettelo / A Phone Book Application

****************************************************************************
*  Tämä sovellus on osa Helsingin Yliopiston ohjelmoinnin MOOC - kurssia.  *
****************************************************************************

Separation of concerns -periaatetta noudatellen koodi tulee jakaa osiin, joista kukin käsittelee omaa asiaansa. Olio-ohjelmoinnin piirissä tätä periaatetta ilmentää niin sanottu yhden vastuun (single responsibility) -periaate. Eli yksittäisen luokan olioiden tulisi olla vastuussa yhdestä reaalimaailman ilmiöstä.

Puhelinluettelossa tälläisiä olisivat esimerkiksi: [henkilö, nimi, puhelinnumero ja puhelinluettelo]

Näistä henkilö voisi olla oma luokkansa, jonka vastuulla on sitoa yhteen tietty nimi ja siihen liittyvät puhelinnumerot.
Puhelinluettelo itsessään voisi olla luokka, jonka vastuulla on hallinnoida henkilöitä.

Nämä kaksi luokkaa muodostavat sovelluksen logiikan.
Sovelluslogiikan muodostavien luokkien lisäksi ohjelmalla on luokka käyttöliittymää varten.

Puhelinluettelon tietojen käsittely on selkeästi oma vastuunsa, joten siihen on myös luokkaansa.