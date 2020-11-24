let lineCount = 0;
function drawLine(event) {
    console.log(lineCount)
    const canvas = document.getElementById('canvas_display');
    const context = canvas.getContext('2d');
    context.moveTo(0,0)
    context.lineTo(200,200)
    context.stroke()
    lineCount++
}