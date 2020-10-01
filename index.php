<?php include("conexao.php");

$consulta = "SELECT * FROM  pagina-web-integrantes";
$con = $mysqli->query($consulta) or die($mysqli->error);

?>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    <h1>Hello world!</h1>
    <table>
      <tr>
        <td>Id</td>
        <td>Titulo</td>
        <td>Resumo</td> 
        <td>Tipo de Pesquisa</td> 
        <td>Periodo</td> 
        <td>Coordenador</td> 
        <td>Parceiros</td> 
        <td>Financiador</td> 
      </tr>
      <?php while($dado = $con->fetch_array()){ ?>
        <tr>
          <td><?php echo $dado["id"]; ?></td>
          <td><?php echo $dado["titulo"]; ?></td>
          <td><?php echo $dado["resumo"]; ?></td>
          <td><?php echo $dado["tipo_de_pesquisa"]; ?></td>
          <td><?php echo $dado["periodo"]; ?></td>
          <td><?php echo $dado["coordenador"]; ?></td>
          <td><?php echo $dado["parceiros"]; ?></td>
          <td><?php echo $dado["financiador"]; ?></td>
        </tr>
      <?php }?>
    </table>
</body>
</html>