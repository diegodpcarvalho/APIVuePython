<template>
  <div class="container">
    <h2>Buscar Dados</h2>

    <!-- Campo de seleção de coluna -->
    <label for="coluna">Escolha a coluna:</label>
    <select v-model="colunaSelecionada">
      <option v-for="coluna in colunas" :key="coluna" :value="coluna">
        {{ coluna }}
      </option>
    </select>

    <!-- Campo de entrada para o termo de busca -->
    <label for="termo">Digite o termo de busca:</label>
    <input type="text" v-model="termoBusca" placeholder="Digite aqui..." />

    <!-- Botão para buscar -->
    <button @click="buscarDados">Buscar</button>

    <!-- Exibir tabela apenas se houver resultados -->
    <table v-if="resultados.length">
      <thead>
        <tr>
          <th v-for="(valor, chave) in resultados[0]" :key="chave">
            {{ chave }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in resultados" :key="index">
          <td v-for="(valor, chave) in item" :key="chave">
            {{ valor }}
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Mensagem caso não haja resultados -->
    <p v-else>Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termoBusca: "",
      colunaSelecionada: "Cidade", // Padrão
      resultados: [],
      colunas: ["Registro_ANS", "CNPJ", "Nome_Fantasia", "Cidade", "UF", "Representante"],
    };
  },
  methods: {
    async buscarDados() {
      if (!this.termoBusca) {
        alert("Digite um termo para buscar!");
        return;
      }

      try {
        const url = `http://127.0.0.1:5000/buscar?q=${this.termoBusca}&coluna=${this.colunaSelecionada}`;
        const resposta = await fetch(url);
        const dados = await resposta.json();
        this.resultados = dados;
      } catch (erro) {
        console.error("Erro ao buscar dados:", erro);
        alert("Erro ao buscar dados. Verifique o console para mais detalhes.");
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
}

label {
  display: block;
  margin-top: 10px;
}

input, select {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}

button {
  margin-top: 10px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>
