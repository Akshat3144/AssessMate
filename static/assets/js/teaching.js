function handleFileSelect(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
  
    reader.onload = function(e) {
      const pdfData = new Uint8Array(e.target.result);
      // Simulate backend processing (e.g., using a PDF processing library)
      const processedText1 = "Processed Text from PDF 1";
      const processedText2 = "Processed Text from PDF 2";
      displayResult(processedText1, processedText2);
    };
  
    reader.readAsArrayBuffer(file);
  }
  
  function displayResult(text1, text2) {
    document.getElementById('text1').innerText = text1;
    document.getElementById('text2').innerText = text2;
  }