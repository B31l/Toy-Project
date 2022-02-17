using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SkullController : MonoBehaviour {

    void Update() {
        if(transform.position.y < -5.0f) {
            Destroy(gameObject);
        } 
    }
}
