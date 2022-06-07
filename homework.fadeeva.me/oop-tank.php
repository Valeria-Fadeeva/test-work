<?php
declare(strict_types=1);

error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');

set_exception_handler(function($exception) {
    // @var Exception $exception
    echo $exception->getMessage(), "\n<br>\n";
    echo $exception->getFile(), ':', $exception->getLine(), "\n<br>\n";
    echo $exception->getTraceAsString(), "\n<br>\n";
});

$a = array(
"Задача:",
"Реализовать объекты:",
"Объект 'Пушка'",
"имеет метод 'load' и 'fire'",
"входящий параметр в методе 'load' - 'Патрон'",
"",
"Объект 'Патрон'",
"наследует базовый класс",
"имеет несколько типов: 'обычный', 'бронебойный', 'трассер'",
"",
"Вдруг подвезли новый тип снарядов, подходящих для загрузки в объект 'Пушка'",
"не наследует базовый класс",
"",
"'Танк', имеющий 'Пушку' и стреляющий разными 'Патронами'",
"Указать тип переменной метода 'load'",
"",
"-------------------------",
);

foreach ($a as $value) {
    echo $value . '<br>';
}


// ОПИСАНИЕ

interface bullet_interface {
    public function get_type();
    public function print_type();
    public function get_power();
}

class bullet implements bullet_interface {
    protected static $type = 'базовый патрон';
    protected static $power = 0;
    
    public function get_type() {
        return static::$type;
    }
    
    public function print_type() {
        return __FUNCTION__ . ' {class name: ' . get_called_class() . '; type: \$bullet = ' . static::$type . '}';
    }
    
    public static function print_parent_type() {
        $pc = get_parent_class() ? get_parent_class() : __CLASS__;
        return __FUNCTION__ . ' {class name: ' . $pc . '; type: \$bullet = ' . self::$type . '}';
    }
    
    public function get_power() {
        return static::$power;
    }
}

class bullet_1_a extends bullet {
    protected static $type = 'обычный патрон';
    protected static $power = 33;
}

class bullet_1_b extends bullet {
    protected static $type = 'бронебойный патрон';
    protected static $power = 50;
}

class bullet_2_a extends bullet {
    protected static $type = 'трассер';
    protected static $light_power = 100;
    
    public function get_light_power() {
        return static::$light_power;
    }
}

class bullet_3_a implements bullet_interface {
    protected static $type = 'супер бронебойный патрон';
    protected static $power = 100;
    protected static $fire_power = 50;
    
    public function get_type() {
        return static::$type;
    }
    
    public function print_type() {
        return __FUNCTION__ . ' {class name: ' . get_called_class() . '; type: \$bullet = ' . static::$type . '}';
    }
    
    public function get_power() {
        return static::$power;
    }
    
    public function get_fire_power() {
        return static::$fire_power;
    }
}

class weapon {
    protected static $bul;
    
    public function print_type() {
        if (!empty(static::$bul)) {
            return __FUNCTION__ . ' {class name: ' . get_called_class() . '; type \$bullet = ' . gettype(static::$bul) . '}';
        } else {
            throw new Exception('Патрон не загружен');
        }
    }

    public function load(object $bullet) {
        if (!empty($bullet)) {
            static::$bul = $bullet;
            return __FUNCTION__ . ' {' . $bullet->print_type() . '}';
        } else {
            throw new Exception('В метод передан аргумент, не являющийся объектом');
        }
    }
    
    public function fire() {
        if (!empty(static::$bul)) {
            return __FUNCTION__ . ' {' . 'Стреляем: ' . static::$bul->get_type() . '}';
        } else {
            throw new Exception('Не задан тип патрона');
        }
    }
}

class tank extends weapon {
    protected static $bul_type;
    
    public function choice_bullet_type(object $b_type) {
        if ($b_type instanceof bullet_interface) {
            static::$bul_type = $b_type;
            return __FUNCTION__ . ' {' . static::$bul_type->print_type() . '}';
        } else {
            throw new Exception('Таких патронов еще не завезли');
        }
    }
    
    public function weapon_load() {
        return __FUNCTION__ . ' {' . $this->load(static::$bul_type) . '}';
    }
    
    public function tank_fire() {
        return $this->fire();
    }
}

class nulllllll {};


// ВЫПОЛНЕНИЕ
$t = new tank();

$bul_1_a = new bullet_1_a();
$bul_1_b = new bullet_1_b();
$bul_2_a = new bullet_2_a();
$bul_3_a = new bullet_3_a();

$bul_4_a = new nulllllll;

$queue = [&$bul_1_a, &$bul_1_b, &$bul_2_a, &$bul_3_a, &$bul_4_a,];

foreach ($queue as $el) {
    echo $t->choice_bullet_type($el);
    echo '<br>';
    echo $t->weapon_load();
    echo '<br>';
    echo $t->tank_fire();
    echo '<br>';
    echo $t->print_type();

    echo '<br>';
    echo '<br>';
}
