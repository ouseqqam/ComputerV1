
function solution () {
    const text = document.getElementById("hello").value
    const equation = text.replaceAll(" ", "")
    const equation1 = equation.split('=')
    const objects = [{
        coef: 0,
        power: 0
    }]
    let d = 0
    for(let j = 0; j < 2;j++)
    {
        for (let i = 0; i < equation1[j].length; i++) {
            const str = []
            let k = 1
            const object = {
                coef: '',
                power: ''
            }
                while (equation1[j][i] != 'X')
                {
                    if (equation1[j][i] == '*')
                    {
                        i++
                        break
                    }
                    else
                        str.push(equation1[j][i++])
                }
                let coef = str.join("")
                if (j == 1)
                    k = -1
                object.coef = k * parseInt(coef)
                if (equation1[j][i] == 'X')
                    i++
                if (equation1[j][i] == '^')
                    object.power = parseInt(equation1[j][++i])
                if (d > 0)
                {
                    for(let x = 1; x < objects.length - 1; x++)
                    {
                        if (objects[x].power == object.power)
                        {
                            console.log("equality")
                        }
                    }
                }
                objects.push(object)
                d++
                console.log(d)
        }
        if (equation1[1] == '0')
        {
           // console.log("hello")
            break
        }
    }
    objects.splice(0, 1)
    console.log(objects)
}
