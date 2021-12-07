import fs from "fs";

function readFile(file) {
    return fs.readFileSync(file, "utf8").split("\n");
}

export default readFile
