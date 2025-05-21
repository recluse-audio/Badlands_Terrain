var filepath = "formatted_matrix.txt";
var x = 0;
var y = 0;

function bang(){
    // First make sure we can open the file
    var file = new File(filepath, 'read', 'TEXT');
    if (!file.isopen) {
      outlet(0, ('Could not open file: ' + filepath + '\n'));
      return;
    }

    // Ok, file is open, now convert it to an array of lines
    var eof = file.eof;
    var lines = [];
    while(file.position < eof) {
      lines.push(file.readline(9999));
    }

    var z = 0;
    // Make an array of the values in each line [x, y, z]
    for(i = 0; i < lines.length; i++){
      var cells = lines[i].split(",");
      if(cells[0] == x && cells[1] == y)
        z = cells[2];
    }

    outlet(0,"x = ", x, "y = ", y, "z = ", z);

}

// function bang() {
//     var file = new File(filepath, 'read', 'TEXT');
//     if (!file.isopen) {
//       error('Could not open file: ' + filepath + '\n');
//       return;
//     }
//     var eof = file.eof;
//     var lines = [];
//     while(file.position < eof) {
//       lines.push(file.readline(9999));
//     }
//     var cells = [];
//     for(i = 0; i < lines.length; i++){
//       cells[i] = lines[i].split(delim);
//     }
//     for(i = 0; i < lines.length; i++){
//       for(j = 0; j < cells[i].length; j++) {
//         if (!isNaN(cells[i][j])) {
//           cells[i][j] = Number(cells[i][j]);
//         }
//         var outArray = [i];
//         outArray = outArray.concat(cells[i]);
//         outlet(0, outArray);
//       }
//     }
//   }