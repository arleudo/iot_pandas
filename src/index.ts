import * as fs from "fs";
import * as path from "path";
import { Pacient } from "./Paciente";

function gerarCsv(nomeArquivo: string, quantidadeRegistros: number): void {
  const pastaAssets = "assets";
  const caminhoArquivo = path.join(pastaAssets, nomeArquivo);

  if (!fs.existsSync(pastaAssets)) {
    fs.mkdirSync(pastaAssets);
  }

  const cabecalho =
    "id;genero;cpf;idade;imc;rendaFamiliar;refluxoGastroesofagico;asma;pancreatite;incontinenciaUrinariaDeEsforco;colelitíase;disfuncaoEretil;sindromeDoOvarioPolicistico;varizes;hipertensaoIntracranianaIdiopatica;depressao;esteatoseHepatica;herniaDeDisco;dislipidemia;apneiaDoSono;infertilidade;ansiedade;doencasCardiovasculares;historicoTromboembolismo;diabetesTipoII;osteoartriteIncapacitante\n";
  fs.writeFileSync(caminhoArquivo, cabecalho, "utf8");

  for (let i = 0; i < quantidadeRegistros; i++) {
    const registro = new Pacient().ToString();
    fs.appendFileSync(caminhoArquivo, registro + "\n", "utf8");
  }

  console.log(
    `Arquivo CSV com ${quantidadeRegistros} registros gerado em ${caminhoArquivo}`
  );
}

gerarCsv("dados.csv", 50);
