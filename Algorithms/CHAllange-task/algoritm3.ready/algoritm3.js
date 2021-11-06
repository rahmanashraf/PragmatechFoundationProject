let birinci = prompt("birinci ededi yaz")
let ikinci = prompt("ikinci ededi yaz")
Number(birinci)
Number(ikinci)

if (30 < birinci && birinci < 70 && 30 < ikinci && ikinci < 70) {
    console.log("Her iksi duzdu")
} else if (30 < birinci && birinci < 70 && 30 < ikinci && ikinci > 70) {
    console.log("biri sehvdi biri duzdu")
} else if (30 < birinci && birinci < 70 && 30 > ikinci && ikinci < 70) {
    console.log("biri sehvdi biri duzdu")
} else if (30 > birinci && birinci < 70 && 30 < ikinci && ikinci < 70) {
    console.log("biri sehvdi biri duzdu")
} else if (30 < birinci && birinci > 70 && 30 < ikinci && ikinci < 70) {
    console.log("biri sehvdi biri duzdu")
} else {
    console.log("ikside sehvdi")
}