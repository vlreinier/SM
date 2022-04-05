using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Valbeweging : MonoBehaviour
{	
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
	public int mass;
	
    // Start is called before the first frame update
    void Start()
    {
        mass = 10;
		Force = new Vector3(0,-15,0);
		transform.position = new Vector3(0,10,0);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
		Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
