package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	fs := http.FileServer(http.Dir("./frontend"))
	http.Handle("/", fs)
	flaghere := "/flagnyaadadisini"
	var arrlen int = len(flaghere)
	slace := make([]byte, arrlen)
	for i := 0; i < len(slace); i++ {
		slace[i] = flaghere[i] + byte(i)
	}
	sliced := []byte{47, 103, 110, 100, 107, 115, 127, 104, 105, 109, 107, 111, 117, 128, 119, 125, 121}
	res := bytes.Compare(slace, sliced)
	if res == 0 {
		http.HandleFunc(flaghere, FlagServe)
		http.ListenAndServe(":14022", nil)
	}
}

func FlagServe(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Congrats! Here is your flag:\nhology3{jU5t_a_s1mpl3_G0laNg_r1ddl3}")
}
