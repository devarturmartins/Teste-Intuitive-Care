<template>
  <div>
    <h1>Agências</h1>
    <div class="search-container">
      <input
        v-model="searchTerm"
        placeholder="Digite um termo para buscar"
        class="search-input"
      />
      <button @click="fetchData" class="search-button">Pesquisar</button>
    </div>
    <table class="table" v-if="agencias.length > 0">
      <thead>
        <tr>
          <th>Registro ANS</th>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Modalidade</th>
          <th>Cidade</th>
          <th>UF</th>
          <th>Telefone</th>
          <th>E-mail</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="agencia in agencias" :key="agencia.Registro_ANS">
          <td>{{ agencia.Registro_ANS }}</td>
          <td>{{ agencia.CNPJ }}</td>
          <td>{{ agencia.Razao_Social }}</td>
          <td>{{ agencia.Nome_Fantasia || "N/A" }}</td>
          <td>{{ agencia.Modalidade }}</td>
          <td>{{ agencia.Cidade }}</td>
          <td>{{ agencia.UF }}</td>
          <td>{{ agencia.Telefone || "N/A" }}</td>
          <td>{{ agencia.Endereco_eletronico || "N/A" }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>Nenhum dado encontrado.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      agencias: [], // Lista de agências retornadas pela API
      searchTerm: "", // Termo de busca digitado pelo usuário
    };
  },
  methods: {
    async fetchData() {
      try {
        // Fazer a requisição para a API com o termo de busca como query
        const response = await axios.get(
          "http://localhost:8000/api/agencias/agencias/",
          {
            params: { term: this.searchTerm },
          }
        );
        console.log("Dados retornados pela API:", response.data); // Verificar os dados no console
        this.agencias = response.data; // Atualizar a lista de agências com os dados retornados
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    },
  },
};
</script>

<style>
.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th,
.table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.table th {
  background-color: #f4f4f4;
}

.search-container {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  padding: 8px;
  width: 100%;
  max-width: 400px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}
</style>