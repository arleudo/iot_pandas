import { v4 as uuid } from "uuid";
import faker from "faker-br";
import {
  ObterGeneroAleatorio,
  ObterRendaFamiliarPonderada,
  ObterImcPonderado,
  ObterIdadePonderada,
  ObterBooleanoAleatorio,
  ObterColelitíase,
  ObterDisfuncaoEretil,
  ObterSindromeDoOvarioPolicistico,
  ObterVarizes,
  ObterHipertensaoIntracranianaIdiopatica,
  ObterEsteatoseHepatica,
  ObterHerniaDeDisco,
  ObterDislipidemia,
  ObterApneiaDoSono,
  ObterInfertilidade,
  ObterAnsiedade,
  ObterDiabetesTipo2,
  ObterOsteoartriteIncapacitante,
} from "./Utils";

export class Pacient {
  private id: string;
  private cpf: string;
  private genero: string;
  private rendaFamiliar: string;
  private imc: number;
  private idade: number;
  private refluxoGastroesofagico: string;
  private asma: string;
  private pancreatite: string;
  private incontinenciaUrinariaDeEsforco: string;
  private colelitíase: string;
  private disfuncaoEretil: string;
  private sindromeDoOvarioPolicistico: string;
  private varizes: string;
  private hipertensaoIntracranianaIdiopatica: string;
  private depressao: string;
  private esteatoseHepatica: string;
  private herniaDeDisco: string;
  private dislipidemia: string;
  private apneiaDoSono: string;
  private infertilidade: string;
  private ansiedade: string;
  private doencasCardiovasculares: string;
  private historicoTromboembolismo: string;
  private diabetesTipoII: string;
  private osteoartriteIncapacitante: string;

  constructor() {
    this.id = uuid();
    this.cpf = faker.br.cpf();
    this.genero = ObterGeneroAleatorio();
    this.rendaFamiliar = ObterRendaFamiliarPonderada();
    this.imc = ObterImcPonderado(this.rendaFamiliar);
    this.idade = ObterIdadePonderada();
    this.refluxoGastroesofagico = ObterBooleanoAleatorio();
    this.asma = ObterBooleanoAleatorio();
    this.pancreatite = ObterBooleanoAleatorio();
    this.incontinenciaUrinariaDeEsforco = ObterBooleanoAleatorio();
    this.colelitíase = ObterColelitíase(this.genero);
    this.disfuncaoEretil = ObterDisfuncaoEretil(this.genero, this.idade);
    this.sindromeDoOvarioPolicistico = ObterSindromeDoOvarioPolicistico(
      this.genero,
      this.idade
    );
    this.varizes = ObterVarizes(this.genero, this.idade);
    this.hipertensaoIntracranianaIdiopatica =
      ObterHipertensaoIntracranianaIdiopatica(
        this.genero,
        this.idade,
        this.imc
      );
    this.depressao = ObterBooleanoAleatorio();
    this.esteatoseHepatica = ObterEsteatoseHepatica();
    this.herniaDeDisco = ObterHerniaDeDisco(this.idade);
    this.dislipidemia = ObterDislipidemia(this.genero, this.idade);
    this.apneiaDoSono = ObterApneiaDoSono(this.idade, this.imc);
    this.infertilidade = ObterInfertilidade(this.idade);
    this.ansiedade = ObterAnsiedade(this.genero);
    this.doencasCardiovasculares = ObterBooleanoAleatorio();
    this.historicoTromboembolismo = ObterBooleanoAleatorio();
    this.diabetesTipoII = ObterDiabetesTipo2(this.imc);
    this.osteoartriteIncapacitante = ObterOsteoartriteIncapacitante(
      this.genero,
      this.idade
    );
  }

  ToString(): string {
    return (
      this.id +
      ";" +
      this.genero +
      ";" +
      this.cpf +
      ";" +
      this.idade +
      ";" +
      this.imc +
      ";" +
      this.rendaFamiliar +
      ";" +
      this.refluxoGastroesofagico +
      ";" +
      this.asma +
      ";" +
      this.pancreatite +
      ";" +
      this.incontinenciaUrinariaDeEsforco +
      ";" +
      this.colelitíase +
      ";" +
      this.disfuncaoEretil +
      ";" +
      this.sindromeDoOvarioPolicistico +
      ";" +
      this.varizes +
      ";" +
      this.hipertensaoIntracranianaIdiopatica +
      ";" +
      this.depressao +
      ";" +
      this.esteatoseHepatica +
      ";" +
      this.herniaDeDisco +
      ";" +
      this.dislipidemia +
      ";" +
      this.apneiaDoSono +
      ";" +
      this.infertilidade +
      ";" +
      this.ansiedade +
      ";" +
      this.doencasCardiovasculares +
      ";" +
      this.historicoTromboembolismo +
      ";" +
      this.diabetesTipoII +
      ";" +
      this.osteoartriteIncapacitante
    );
  }
}
