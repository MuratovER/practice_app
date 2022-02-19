function show_hide(id_1)
{
    if(document.getElementById(id_1).style.display=="none")
    {
        document.getElementById(id_1).style.display="flex";
    }
    else
    {
        document.getElementById(id_1).style.display="none";
    }
}