import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    # --- Konstruktorin (__init__) testit ---

    def test_konstruktori_luo_tyhjan_varaston(self):
        # Normaali luonti, tilavuus > 0 ja alku_saldo = 0
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_virheellinen_tilavuus_nollataan(self):
        # Haara: tilavuus <= 0.0
        huono_varasto = Varasto(-10.0)
        self.assertAlmostEqual(huono_varasto.tilavuus, 0.0)

    def test_konstruktori_virheellinen_alkusaldo_nollataan(self):
        # Haara: alku_saldo < 0.0
        huono_varasto = Varasto(10.0, -5.0)
        self.assertAlmostEqual(huono_varasto.saldo, 0.0)

    def test_konstruktori_alkusaldo_suurempi_kuin_tilavuus(self):
        # Haara: alku_saldo > tilavuus
        huono_varasto = Varasto(10.0, 15.0)
        self.assertAlmostEqual(huono_varasto.saldo, 10.0)

    def test_konstruktori_alkusaldo_mahtuu(self):
        # Haara: alku_saldo <= tilavuus
        uusi_varasto = Varasto(10.0, 5.0)
        self.assertAlmostEqual(uusi_varasto.saldo, 5.0)

    # --- lisaa_varastoon -metodin testit ---

    def test_lisaa_negatiivinen_maara_ei_muuta_saldoa(self):
        # Haara: maara < 0
        self.varasto.lisaa_varastoon(-5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_lisaa_saldoa_kun_mahtuu(self):
        # Haara: maara <= paljonko_mahtuu()
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_enemman_kuin_mahtuu_laittaa_tayteen(self):
        # Haara: maara > paljonko_mahtuu() (else)
        self.varasto.lisaa_varastoon(15.0)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)

    # --- ota_varastosta -metodin testit ---

    def test_ota_negatiivinen_maara_palauttaa_nollan(self):
        # Haara: maara < 0
        saatu = self.varasto.ota_varastosta(-5.0)
        self.assertAlmostEqual(saatu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ota_enemman_kuin_saldoa_on_antaa_kaiken(self):
        # Haara: maara > self.saldo
        self.varasto.lisaa_varastoon(5.0)
        saatu = self.varasto.ota_varastosta(10.0)
        self.assertAlmostEqual(saatu, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        # Haara: normaali otto
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu, 2)
        self.assertAlmostEqual(self.varasto.saldo, 6)

    # --- Apumetodien testit ---

    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        # Testaa __str__ metodin palautusarvo
        self.varasto.lisaa_varastoon(5.0)
        self.assertEqual(str(self.varasto), "saldo = 5.0, vielä tilaa 5.0")
