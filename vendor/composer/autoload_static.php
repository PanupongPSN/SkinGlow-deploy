<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit09a54dc6f72fa2ddfa52f9df0b74ec3f
{
    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInit09a54dc6f72fa2ddfa52f9df0b74ec3f::$classMap;

        }, null, ClassLoader::class);
    }
}
